import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import threading
import time
import os
import ctypes
from pynput import mouse, keyboard
import keyboard as kb
import mouse as ms

class FinalNoRecoilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Strong No Recoil - Final Gaming Utility")
        self.root.geometry("600x700")
        self.root.configure(bg='#1a1a2e')  # Dark blue background
        self.root.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # App state
        self.app_running = False
        self.recoil_active = False
        self.rapid_fire_active = False
        self.sleep_mode = False
        
        # Variables
        self.recoil_enabled = tk.BooleanVar(value=False)
        self.rapid_fire_enabled = tk.BooleanVar(value=False)
        self.require_ads = tk.BooleanVar(value=True)
        self.sleep_enabled = tk.BooleanVar(value=False)
        
        self.vertical_strength = tk.IntVar(value=8)
        self.horizontal_strength = tk.IntVar(value=2)
        self.recoil_delay = tk.DoubleVar(value=0.01)
        self.rapid_fire_speed = tk.IntVar(value=50)
        self.sleep_delay = tk.DoubleVar(value=0.1)
        
        self.current_mode = tk.StringVar(value="HEAVY")
        self.config_slot = tk.IntVar(value=1)
        
        # Threading
        self.recoil_thread = None
        self.rapid_fire_thread = None
        self.running = False
        
        # Mode presets
        self.modes = {
            "LIGHT": {"vertical": 3, "horizontal": 1, "delay": 0.02},
            "MEDIUM": {"vertical": 6, "horizontal": 2, "delay": 0.015},
            "HEAVY": {"vertical": 8, "horizontal": 2, "delay": 0.01}
        }
        
        # System detection
        self.is_64bit = self.check_system_architecture()
        
        # Create startup screen
        self.create_startup_screen()
        
    def check_system_architecture(self):
        """Check if system is 64-bit or 32-bit"""
        try:
            return ctypes.sizeof(ctypes.c_void_p) == 8
        except:
            return False
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_startup_screen(self):
        """Create startup screen with logo and loading"""
        self.startup_frame = tk.Frame(self.root, bg='#1a1a2e')
        self.startup_frame.pack(fill='both', expand=True)
        
        # Logo and title
        logo_label = tk.Label(self.startup_frame, text="🎯", font=('Arial', 48), 
                             fg='#ff6b6b', bg='#1a1a2e')
        logo_label.pack(pady=(100, 20))
        
        title_label = tk.Label(self.startup_frame, text="STRONG NO RECOIL", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ff6b6b', bg='#1a1a2e')
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(self.startup_frame, text="Final Gaming Utility", 
                                 font=('Arial', 12), 
                                 fg='#cccccc', bg='#1a1a2e')
        subtitle_label.pack(pady=(0, 20))
        
        # System info
        arch_text = "64-bit System" if self.is_64bit else "32-bit System"
        arch_label = tk.Label(self.startup_frame, text=arch_text, 
                             font=('Arial', 10), 
                             fg='#4ecdc4', bg='#1a1a2e')
        arch_label.pack(pady=(0, 30))
        
        # Loading bar
        self.loading_frame = tk.Frame(self.startup_frame, bg='#2a2a3e', height=20)
        self.loading_frame.pack(fill='x', padx=100, pady=20)
        
        self.progress_bar = tk.Frame(self.loading_frame, bg='#ff6b6b', width=0)
        self.progress_bar.pack(side='left', fill='y')
        
        # Status text
        self.status_label = tk.Label(self.startup_frame, text="Initializing...", 
                                    font=('Arial', 10), 
                                    fg='#888888', bg='#1a1a2e')
        self.status_label.pack(pady=20)
        
        # Start initialization
        self.root.after(100, self.initialize_app)
        
    def initialize_app(self):
        """Initialize the application with loading animation"""
        steps = [
            ("Loading modules...", 0.2),
            ("Detecting system architecture...", 0.4),
            ("Setting up game controls...", 0.6),
            ("Preparing interface...", 0.8),
            ("Starting application...", 1.0)
        ]
        
        def update_progress(step_index):
            if step_index < len(steps):
                text, progress = steps[step_index]
                self.status_label.config(text=text)
                
                # Update progress bar
                width = int(progress * 400)
                self.progress_bar.config(width=width)
                
                if step_index < len(steps) - 1:
                    self.root.after(500, lambda: update_progress(step_index + 1))
                else:
                    self.root.after(1000, self.show_main_interface)
        
        update_progress(0)
        
    def show_main_interface(self):
        """Show the main application interface"""
        self.startup_frame.destroy()
        self.setup_ui()
        self.load_config()
        self.app_running = True
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a2e', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Header with logo
        header_frame = tk.Frame(main_frame, bg='#1a1a2e')
        header_frame.pack(fill='x', pady=(0, 20))
        
        logo_label = tk.Label(header_frame, text="🎯", font=('Arial', 24), 
                             fg='#ff6b6b', bg='#1a1a2e')
        logo_label.pack(side='left')
        
        title_frame = tk.Frame(header_frame, bg='#1a1a2e')
        title_frame.pack(side='left', padx=(10, 0))
        
        title_label = tk.Label(title_frame, text="STRONG NO RECOIL", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff6b6b', bg='#1a1a2e')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Final Gaming Utility", 
                                 font=('Arial', 10), 
                                 fg='#cccccc', bg='#1a1a2e')
        subtitle_label.pack()
        
        # System info
        arch_text = "64-bit" if self.is_64bit else "32-bit"
        arch_label = tk.Label(title_frame, text=f"System: {arch_text}", 
                             font=('Arial', 8), 
                             fg='#4ecdc4', bg='#1a1a2e')
        arch_label.pack()
        
        # Main toggle switch
        toggle_frame = tk.Frame(main_frame, bg='#2a2a3e', relief='raised', bd=2)
        toggle_frame.pack(fill='x', pady=(0, 20))
        
        self.toggle_button = tk.Button(toggle_frame, text="🔴 STOPPED", 
                                      font=('Arial', 14, 'bold'),
                                      bg='#ff6b6b', fg='#ffffff',
                                      relief='flat', padx=20, pady=10,
                                      command=self.toggle_app)
        self.toggle_button.pack(pady=10)
        
        # Status indicator
        self.status_indicator = tk.Label(toggle_frame, text="Application Ready", 
                                        font=('Arial', 10), 
                                        fg='#4ecdc4', bg='#2a2a3e')
        self.status_indicator.pack(pady=(0, 10))
        
        # Configuration Section
        config_frame = self.create_section(main_frame, "⚙️ CONFIGURATION")
        
        config_buttons_frame = tk.Frame(config_frame, bg='#2a2a3e')
        config_buttons_frame.pack(fill='x', pady=5)
        
        tk.Button(config_buttons_frame, text="📁 LOAD CONFIG", 
                 command=self.load_config, bg='#404050', fg='#ffffff',
                 relief='flat', padx=10, pady=5).pack(side='left', padx=(0, 10))
        
        tk.Button(config_buttons_frame, text="💾 SAVE CONFIG", 
                 command=self.save_config, bg='#404050', fg='#ffffff',
                 relief='flat', padx=10, pady=5).pack(side='left')
        
        # Config slot selector
        slot_frame = tk.Frame(config_frame, bg='#2a2a3e')
        slot_frame.pack(fill='x', pady=5)
        
        tk.Label(slot_frame, text="Slot:", bg='#2a2a3e', fg='#ffffff').pack(side='left')
        slot_spinbox = tk.Spinbox(slot_frame, from_=1, to=10, width=5,
                                 textvariable=self.config_slot, bg='#404050', fg='#ffffff')
        slot_spinbox.pack(side='left', padx=(5, 0))
        
        # Anti-Recoil Section
        recoil_frame = self.create_section(main_frame, "🎯 ANTI-RECOIL")
        
        # Toggle controls
        tk.Checkbutton(recoil_frame, text="🔫 TOGGLE RECOIL SCRIPT", 
                      variable=self.recoil_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(recoil_frame, text="🎯 REQUIRE ADS (Aim Down Sight)", 
                      variable=self.require_ads, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        # Sleep mode
        tk.Checkbutton(recoil_frame, text="😴 SLEEP MODE (Delay between shots)", 
                      variable=self.sleep_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        # Strength controls
        strength_frame = tk.Frame(recoil_frame, bg='#2a2a3e')
        strength_frame.pack(fill='x', pady=10)
        
        tk.Label(strength_frame, text="📈 VERTICAL STRENGTH:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.vertical_strength, 0, 15)
        
        tk.Label(strength_frame, text="📊 HORIZONTAL STRENGTH:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.horizontal_strength, 0, 10)
        
        tk.Label(strength_frame, text="⏱️ RECOIL DELAY:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.recoil_delay, 0.001, 0.05, True)
        
        tk.Label(strength_frame, text="😴 SLEEP DELAY:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.sleep_delay, 0.01, 0.5, True)
        
        # Mode selection
        mode_frame = tk.Frame(recoil_frame, bg='#2a2a3e')
        mode_frame.pack(fill='x', pady=10)
        
        tk.Label(mode_frame, text="🎮 MODE:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        
        mode_buttons_frame = tk.Frame(mode_frame, bg='#2a2a3e')
        mode_buttons_frame.pack(fill='x', pady=5)
        
        for mode in ["LIGHT", "MEDIUM", "HEAVY"]:
            tk.Button(mode_buttons_frame, text=mode, 
                     command=lambda m=mode: self.set_mode(m),
                     bg='#404050', fg='#ffffff', relief='flat', padx=10, pady=5).pack(side='left', padx=(0, 5))
        
        # Rapid Fire Section
        rapid_frame = self.create_section(main_frame, "🔥 RAPID FIRE")
        
        tk.Checkbutton(rapid_frame, text="🔥 TOGGLE RAPID FIRE", 
                      variable=self.rapid_fire_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Label(rapid_frame, text="⚡ FIRE SPEED:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(rapid_frame, self.rapid_fire_speed, 10, 200)
        
        # Hotkeys Section
        hotkey_frame = self.create_section(main_frame, "⌨️ HOTKEYS")
        
        hotkey_info = tk.Label(hotkey_frame, 
                              text="• INSERT: Toggle app on/off\n• MOUSE1: Rapid fire\n• MOUSE2: ADS requirement\n• F1: Toggle recoil",
                              font=('Arial', 10), 
                              fg='#cccccc', bg='#2a2a3e', justify='left')
        hotkey_info.pack(anchor='w', pady=5)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener for hotkeys"""
        def on_press(key):
            try:
                if key == keyboard.Key.insert:
                    self.toggle_app()
                elif key == keyboard.Key.f1:
                    self.toggle_recoil()
            except AttributeError:
                pass
        
        self.keyboard_listener = keyboard.Listener(on_press=on_press)
        self.keyboard_listener.start()
        
    def toggle_app(self):
        """Toggle the application on/off"""
        if not self.app_running:
            self.app_running = True
            self.toggle_button.config(text="🟢 RUNNING", bg='#4ecdc4')
            self.status_indicator.config(text="Application Active", fg='#4ecdc4')
            messagebox.showinfo("Started", "Application is now running!\nUse INSERT to toggle app.\nUse F1 to toggle recoil.")
        else:
            self.app_running = False
            self.toggle_button.config(text="🔴 STOPPED", bg='#ff6b6b')
            self.status_indicator.config(text="Application Stopped", fg='#ff6b6b')
            self.stop_recoil()
            self.stop_rapid_fire()
            messagebox.showinfo("Stopped", "Application has been stopped.")
    
    def create_section(self, parent, title):
        """Create a section with title"""
        section_frame = tk.Frame(parent, bg='#2a2a3e', relief='raised', bd=2)
        section_frame.pack(fill='x', pady=10)
        
        title_label = tk.Label(section_frame, text=title, 
                              font=('Arial', 12, 'bold'), 
                              fg='#ff6b6b', bg='#2a2a3e')
        title_label.pack(pady=5)
        
        content_frame = tk.Frame(section_frame, bg='#2a2a3e', padx=10, pady=10)
        content_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        return content_frame
    
    def create_slider_with_entry(self, parent, variable, min_val, max_val, is_float=False):
        """Create slider with entry field"""
        frame = tk.Frame(parent, bg='#2a2a3e')
        frame.pack(fill='x', pady=2)
        
        if is_float:
            slider = tk.Scale(frame, from_=min_val, to=max_val, resolution=0.001,
                            variable=variable, orient='horizontal', bg='#2a2a3e', fg='#ffffff',
                            highlightbackground='#2a2a3e', troughcolor='#404050')
        else:
            slider = tk.Scale(frame, from_=min_val, to=max_val,
                            variable=variable, orient='horizontal', bg='#2a2a3e', fg='#ffffff',
                            highlightbackground='#2a2a3e', troughcolor='#404050')
        
        slider.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        if is_float:
            entry = tk.Entry(frame, textvariable=variable, width=8, bg='#404050', fg='#ffffff')
        else:
            entry = tk.Entry(frame, textvariable=variable, width=8, bg='#404050', fg='#ffffff')
        
        entry.pack(side='right')
    
    def set_mode(self, mode):
        """Set recoil mode"""
        if mode in self.modes:
            self.current_mode.set(mode)
            preset = self.modes[mode]
            self.vertical_strength.set(preset["vertical"])
            self.horizontal_strength.set(preset["horizontal"])
            self.recoil_delay.set(preset["delay"])
    
    def toggle_recoil(self):
        """Toggle recoil on/off"""
        if self.recoil_enabled.get():
            self.start_recoil()
        else:
            self.stop_recoil()
    
    def start_recoil(self):
        """Start recoil control"""
        if not self.running:
            self.running = True
            self.recoil_thread = threading.Thread(target=self.recoil_loop)
            self.recoil_thread.daemon = True
            self.recoil_thread.start()
    
    def stop_recoil(self):
        """Stop recoil control"""
        self.running = False
        if self.recoil_thread:
            self.recoil_thread.join()
    
    def stop_rapid_fire(self):
        """Stop rapid fire control"""
        self.running = False
        if self.rapid_fire_thread:
            self.rapid_fire_thread.join()
    
    def check_mouse_button(self, button):
        """Check if mouse button is pressed using improved method"""
        try:
            # Use keyboard library for better game detection
            return kb.is_pressed(button)
        except:
            try:
                # Fallback to mouse library
                return ms.is_pressed(button)
            except:
                return False
    
    def move_mouse(self, dx, dy):
        """Move mouse using improved method"""
        try:
            # Use mouse library for movement
            ms.move(dx, dy, absolute=False)
        except:
            # Fallback method
            pass
    
    def recoil_loop(self):
        """Recoil control loop with improved game detection and sleep"""
        while self.running:
            if self.recoil_enabled.get() and self.app_running:
                # Check if left mouse button is pressed (firing)
                if self.check_mouse_button('left'):
                    # Check ADS requirement
                    if not self.require_ads.get() or self.check_mouse_button('right'):
                        # Get current settings
                        vertical = self.vertical_strength.get()
                        horizontal = self.horizontal_strength.get()
                        delay = self.recoil_delay.get()
                        sleep_delay = self.sleep_delay.get()
                        
                        # Move mouse to compensate recoil
                        self.move_mouse(horizontal, vertical)
                        time.sleep(delay)
                        
                        # Add sleep mode delay if enabled
                        if self.sleep_enabled.get():
                            time.sleep(sleep_delay)
            time.sleep(0.01)
    
    def rapid_fire_loop(self):
        """Rapid fire loop with improved detection"""
        while self.running:
            if self.rapid_fire_enabled.get() and self.app_running:
                if self.check_mouse_button('left'):
                    # Simulate rapid fire
                    speed = self.rapid_fire_speed.get()
                    time.sleep(1.0 / speed)
            time.sleep(0.01)
    
    def save_config(self):
        """Save configuration to file"""
        config = {
            "recoil_enabled": self.recoil_enabled.get(),
            "rapid_fire_enabled": self.rapid_fire_enabled.get(),
            "require_ads": self.require_ads.get(),
            "sleep_enabled": self.sleep_enabled.get(),
            "vertical_strength": self.vertical_strength.get(),
            "horizontal_strength": self.horizontal_strength.get(),
            "recoil_delay": self.recoil_delay.get(),
            "sleep_delay": self.sleep_delay.get(),
            "rapid_fire_speed": self.rapid_fire_speed.get(),
            "current_mode": self.current_mode.get()
        }
        
        slot = self.config_slot.get()
        filename = f"config_{slot}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump(config, f, indent=2)
            messagebox.showinfo("Success", f"Configuration saved to slot {slot}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {e}")
    
    def load_config(self):
        """Load configuration from file"""
        slot = self.config_slot.get()
        filename = f"config_{slot}.json"
        
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    config = json.load(f)
                
                self.recoil_enabled.set(config.get("recoil_enabled", False))
                self.rapid_fire_enabled.set(config.get("rapid_fire_enabled", False))
                self.require_ads.set(config.get("require_ads", True))
                self.sleep_enabled.set(config.get("sleep_enabled", False))
                self.vertical_strength.set(config.get("vertical_strength", 8))
                self.horizontal_strength.set(config.get("horizontal_strength", 2))
                self.recoil_delay.set(config.get("recoil_delay", 0.01))
                self.sleep_delay.set(config.get("sleep_delay", 0.1))
                self.rapid_fire_speed.set(config.get("rapid_fire_speed", 50))
                self.current_mode.set(config.get("current_mode", "HEAVY"))
                
                messagebox.showinfo("Success", f"Configuration loaded from slot {slot}")
            else:
                messagebox.showinfo("Info", f"No configuration found in slot {slot}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load configuration: {e}")
    
    def on_closing(self):
        """Handle application closing"""
        if self.app_running:
            if messagebox.askokcancel("Quit", "Application is running. Do you want to quit?"):
                self.stop_recoil()
                self.stop_rapid_fire()
                if hasattr(self, 'keyboard_listener'):
                    self.keyboard_listener.stop()
                self.root.destroy()
        else:
            if hasattr(self, 'keyboard_listener'):
                self.keyboard_listener.stop()
            self.root.destroy()

def main():
    root = tk.Tk()
    app = FinalNoRecoilApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 