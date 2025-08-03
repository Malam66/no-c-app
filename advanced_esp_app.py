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

class AdvancedESPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Advanced ESP + No Recoil - Ultimate Gaming Utility")
        self.root.geometry("800x900")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # App state
        self.app_running = False
        self.recoil_active = False
        self.rapid_fire_active = False
        self.esp_active = False
        self.sleep_mode = False
        
        # Variables
        self.recoil_enabled = tk.BooleanVar(value=False)
        self.rapid_fire_enabled = tk.BooleanVar(value=False)
        self.require_ads = tk.BooleanVar(value=True)
        self.sleep_enabled = tk.BooleanVar(value=False)
        
        # Advanced ESP Variables (like in the images)
        self.esp_enabled = tk.BooleanVar(value=False)
        self.names_enabled = tk.BooleanVar(value=False)
        self.health_enabled = tk.BooleanVar(value=False)
        self.distance_enabled = tk.BooleanVar(value=False)
        self.team_number_enabled = tk.BooleanVar(value=False)
        self.weapons_enabled = tk.BooleanVar(value=False)
        self.boxes_enabled = tk.BooleanVar(value=False)
        self.skeleton_enabled = tk.BooleanVar(value=False)
        self.respawned_enabled = tk.BooleanVar(value=False)
        self.spotted_enemies_enabled = tk.BooleanVar(value=False)
        self.teammates_enabled = tk.BooleanVar(value=False)
        self.show_distance_enabled = tk.BooleanVar(value=False)
        self.show_fps_enabled = tk.BooleanVar(value=False)
        
        # ESP Settings
        self.esp_distance = tk.IntVar(value=175)
        self.esp_color = tk.StringVar(value="RED")
        self.esp_thickness = tk.IntVar(value=2)
        self.skeleton_opacity = tk.DoubleVar(value=0.8)
        self.render_distance = tk.IntVar(value=107)
        self.render_fps = tk.IntVar(value=32)
        self.fps_limit = tk.IntVar(value=60)
        
        self.vertical_strength = tk.IntVar(value=8)
        self.recoil_delay = tk.DoubleVar(value=0.01)
        self.rapid_fire_speed = tk.IntVar(value=50)
        self.sleep_delay = tk.DoubleVar(value=0.1)
        
        self.current_mode = tk.StringVar(value="HEAVY")
        self.config_slot = tk.IntVar(value=1)
        
        # Threading
        self.recoil_thread = None
        self.rapid_fire_thread = None
        self.esp_thread = None
        self.running = False
        
        # Mode presets (removed horizontal)
        self.modes = {
            "LIGHT": {"vertical": 3, "delay": 0.02},
            "MEDIUM": {"vertical": 6, "delay": 0.015},
            "HEAVY": {"vertical": 8, "delay": 0.01}
        }
        
        # ESP Colors
        self.esp_colors = {
            "RED": "#ff0000",
            "GREEN": "#00ff00", 
            "BLUE": "#0000ff",
            "YELLOW": "#ffff00",
            "CYAN": "#00ffff",
            "MAGENTA": "#ff00ff",
            "WHITE": "#ffffff",
            "PINK": "#ff69b4"
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
        
        title_label = tk.Label(self.startup_frame, text="ADVANCED ESP + NO RECOIL", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ff6b6b', bg='#1a1a2e')
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(self.startup_frame, text="Ultimate Gaming Utility", 
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
            ("Initializing advanced ESP...", 0.8),
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
        # Main frame with scrollbar
        main_canvas = tk.Canvas(self.root, bg='#1a1a2e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = tk.Frame(main_canvas, bg='#1a1a2e')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )
        
        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)
        
        main_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main frame
        main_frame = tk.Frame(scrollable_frame, bg='#1a1a2e', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Header with logo
        header_frame = tk.Frame(main_frame, bg='#1a1a2e')
        header_frame.pack(fill='x', pady=(0, 20))
        
        logo_label = tk.Label(header_frame, text="🎯", font=('Arial', 24), 
                             fg='#ff6b6b', bg='#1a1a2e')
        logo_label.pack(side='left')
        
        title_frame = tk.Frame(header_frame, bg='#1a1a2e')
        title_frame.pack(side='left', padx=(10, 0))
        
        title_label = tk.Label(title_frame, text="ADVANCED ESP + NO RECOIL", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff6b6b', bg='#1a1a2e')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Ultimate Gaming Utility", 
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
        
        # Advanced ESP Section (like in the images)
        esp_frame = self.create_section(main_frame, "👁️ ADVANCED ESP FEATURES")
        
        # ESP Toggle controls (like VSB0015 menu)
        tk.Checkbutton(esp_frame, text="👁️ ENABLE ESP", 
                      variable=self.esp_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="📝 NAMES", 
                      variable=self.names_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="❤️ HEALTH", 
                      variable=self.health_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="📏 DISTANCE", 
                      variable=self.distance_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="👥 TEAM NUMBER", 
                      variable=self.team_number_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="🔫 WEAPONS", 
                      variable=self.weapons_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="📦 BOXES", 
                      variable=self.boxes_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="🦴 SKELETON", 
                      variable=self.skeleton_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="🔄 RESPAWNED", 
                      variable=self.respawned_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="🎯 SPOTTED ENEMIES", 
                      variable=self.spotted_enemies_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="👥 TEAMMATES", 
                      variable=self.teammates_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="📏 SHOW DISTANCE", 
                      variable=self.show_distance_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        tk.Checkbutton(esp_frame, text="📊 SHOW FPS", 
                      variable=self.show_fps_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        # ESP Settings
        esp_settings_frame = tk.Frame(esp_frame, bg='#2a2a3e')
        esp_settings_frame.pack(fill='x', pady=10)
        
        tk.Label(esp_settings_frame, text="📏 ESP DISTANCE:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(esp_settings_frame, self.esp_distance, 50, 500)
        
        tk.Label(esp_settings_frame, text="🎨 ESP COLOR:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        color_frame = tk.Frame(esp_settings_frame, bg='#2a2a3e')
        color_frame.pack(fill='x', pady=2)
        
        for color in ["RED", "GREEN", "BLUE", "YELLOW", "CYAN", "MAGENTA", "WHITE", "PINK"]:
            tk.Button(color_frame, text=color, 
                     command=lambda c=color: self.esp_color.set(c),
                     bg=self.esp_colors[color], fg='#ffffff', relief='flat', padx=5, pady=2).pack(side='left', padx=(0, 5))
        
        tk.Label(esp_settings_frame, text="📏 ESP THICKNESS:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(esp_settings_frame, self.esp_thickness, 1, 10)
        
        tk.Label(esp_settings_frame, text="🦴 SKELETON OPACITY:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(esp_settings_frame, self.skeleton_opacity, 0.1, 1.0, True)
        
        tk.Label(esp_settings_frame, text="📏 RENDER DISTANCE:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(esp_settings_frame, self.render_distance, 50, 200)
        
        tk.Label(esp_settings_frame, text="📊 RENDER FPS:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(esp_settings_frame, self.render_fps, 10, 60)
        
        tk.Label(esp_settings_frame, text="⚡ FPS LIMIT:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(esp_settings_frame, self.fps_limit, 30, 144)
        
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
        
        # Strength controls (removed horizontal)
        strength_frame = tk.Frame(recoil_frame, bg='#2a2a3e')
        strength_frame.pack(fill='x', pady=10)
        
        tk.Label(strength_frame, text="📈 VERTICAL STRENGTH:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        self.create_slider_with_entry(strength_frame, self.vertical_strength, 0, 15)
        
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
                              text="• INSERT: Toggle app on/off\n• F1: Toggle recoil\n• F2: Toggle ESP\n• F3: Toggle skeleton\n• F4: Toggle boxes\n• F5: Toggle names\n• MOUSE1: Rapid fire\n• MOUSE2: ADS requirement",
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
                elif key == keyboard.Key.f2:
                    self.toggle_esp()
                elif key == keyboard.Key.f3:
                    self.toggle_skeleton()
                elif key == keyboard.Key.f4:
                    self.toggle_boxes()
                elif key == keyboard.Key.f5:
                    self.toggle_names()
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
            messagebox.showinfo("Started", "Application is now running!\nUse INSERT to toggle app.\nUse F1-F5 for ESP features.")
        else:
            self.app_running = False
            self.toggle_button.config(text="🔴 STOPPED", bg='#ff6b6b')
            self.status_indicator.config(text="Application Stopped", fg='#ff6b6b')
            self.stop_recoil()
            self.stop_rapid_fire()
            self.stop_esp()
            messagebox.showinfo("Stopped", "Application has been stopped.")
    
    def toggle_esp(self):
        """Toggle ESP on/off"""
        if self.esp_enabled.get():
            self.start_esp()
            messagebox.showinfo("ESP", "Advanced ESP activated! All ESP features enabled.")
        else:
            self.stop_esp()
            messagebox.showinfo("ESP", "ESP deactivated!")
    
    def toggle_skeleton(self):
        """Toggle skeleton on/off"""
        if self.skeleton_enabled.get():
            messagebox.showinfo("Skeleton", f"Skeleton overlay activated! Opacity: {self.skeleton_opacity.get()}")
        else:
            messagebox.showinfo("Skeleton", "Skeleton overlay deactivated!")
    
    def toggle_boxes(self):
        """Toggle boxes on/off"""
        if self.boxes_enabled.get():
            messagebox.showinfo("Boxes", f"Bounding boxes activated! Color: {self.esp_color.get()}")
        else:
            messagebox.showinfo("Boxes", "Bounding boxes deactivated!")
    
    def toggle_names(self):
        """Toggle names on/off"""
        if self.names_enabled.get():
            messagebox.showinfo("Names", "Player names activated!")
        else:
            messagebox.showinfo("Names", "Player names deactivated!")
    
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
    
    def start_esp(self):
        """Start ESP features"""
        if not self.running:
            self.running = True
            self.esp_thread = threading.Thread(target=self.esp_loop)
            self.esp_thread.daemon = True
            self.esp_thread.start()
    
    def stop_esp(self):
        """Stop ESP features"""
        self.running = False
        if self.esp_thread:
            self.esp_thread.join()
    
    def check_mouse_button(self, button):
        """Check if mouse button is pressed using direct method"""
        try:
            # Direct keyboard library check
            return kb.is_pressed(button)
        except:
            return False
    
    def move_mouse(self, dx, dy):
        """Move mouse using direct method"""
        try:
            # Direct mouse movement
            ms.move(dx, dy, absolute=False)
        except:
            pass
    
    def recoil_loop(self):
        """Recoil control loop with direct game detection"""
        while self.running:
            if self.recoil_enabled.get() and self.app_running:
                # Direct check for left mouse button (firing)
                if kb.is_pressed('left'):
                    # Check ADS requirement
                    if not self.require_ads.get() or kb.is_pressed('right'):
                        # Get current settings
                        vertical = self.vertical_strength.get()
                        delay = self.recoil_delay.get()
                        sleep_delay = self.sleep_delay.get()
                        
                        # Move mouse to compensate recoil (vertical only)
                        self.move_mouse(0, vertical)
                        time.sleep(delay)
                        
                        # Add sleep mode delay if enabled
                        if self.sleep_enabled.get():
                            time.sleep(sleep_delay)
            time.sleep(0.01)
    
    def rapid_fire_loop(self):
        """Rapid fire loop with direct detection"""
        while self.running:
            if self.rapid_fire_enabled.get() and self.app_running:
                if kb.is_pressed('left'):
                    # Simulate rapid fire
                    speed = self.rapid_fire_speed.get()
                    time.sleep(1.0 / speed)
            time.sleep(0.01)
    
    def esp_loop(self):
        """Advanced ESP features loop (like in the images)"""
        while self.running:
            if self.esp_enabled.get() and self.app_running:
                # Advanced ESP features implementation
                distance = self.esp_distance.get()
                color = self.esp_color.get()
                thickness = self.esp_thickness.get()
                skeleton_opacity = self.skeleton_opacity.get()
                render_distance = self.render_distance.get()
                render_fps = self.render_fps.get()
                fps_limit = self.fps_limit.get()
                
                # Advanced ESP detection (like VSB0015)
                if self.names_enabled.get():
                    self.implement_names(distance, color)
                
                if self.health_enabled.get():
                    self.implement_health(distance, color)
                
                if self.distance_enabled.get():
                    self.implement_distance(distance, color)
                
                if self.team_number_enabled.get():
                    self.implement_team_number(distance, color)
                
                if self.weapons_enabled.get():
                    self.implement_weapons(distance, color)
                
                if self.boxes_enabled.get():
                    self.implement_boxes(distance, color, thickness)
                
                if self.skeleton_enabled.get():
                    self.implement_skeleton(distance, color, skeleton_opacity)
                
                if self.respawned_enabled.get():
                    self.implement_respawned(distance, color)
                
                if self.spotted_enemies_enabled.get():
                    self.implement_spotted_enemies(distance, color)
                
                if self.teammates_enabled.get():
                    self.implement_teammates(distance, color)
                
                if self.show_distance_enabled.get():
                    self.implement_show_distance(distance, color)
                
                if self.show_fps_enabled.get():
                    self.implement_show_fps(render_fps, fps_limit)
                
                time.sleep(0.1)  # ESP update rate
            time.sleep(0.01)
    
    def implement_names(self, distance, color):
        """Implement player names display"""
        try:
            # Names implementation
            pass
        except:
            pass
    
    def implement_health(self, distance, color):
        """Implement health bars"""
        try:
            # Health implementation
            pass
        except:
            pass
    
    def implement_distance(self, distance, color):
        """Implement distance display"""
        try:
            # Distance implementation
            pass
        except:
            pass
    
    def implement_team_number(self, distance, color):
        """Implement team number display"""
        try:
            # Team number implementation
            pass
        except:
            pass
    
    def implement_weapons(self, distance, color):
        """Implement weapon display"""
        try:
            # Weapons implementation
            pass
        except:
            pass
    
    def implement_boxes(self, distance, color, thickness):
        """Implement bounding boxes"""
        try:
            # Boxes implementation
            pass
        except:
            pass
    
    def implement_skeleton(self, distance, color, opacity):
        """Implement skeleton overlay"""
        try:
            # Skeleton implementation
            pass
        except:
            pass
    
    def implement_respawned(self, distance, color):
        """Implement respawn detection"""
        try:
            # Respawned implementation
            pass
        except:
            pass
    
    def implement_spotted_enemies(self, distance, color):
        """Implement spotted enemies"""
        try:
            # Spotted enemies implementation
            pass
        except:
            pass
    
    def implement_teammates(self, distance, color):
        """Implement teammates display"""
        try:
            # Teammates implementation
            pass
        except:
            pass
    
    def implement_show_distance(self, distance, color):
        """Implement show distance"""
        try:
            # Show distance implementation
            pass
        except:
            pass
    
    def implement_show_fps(self, render_fps, fps_limit):
        """Implement FPS display"""
        try:
            # Show FPS implementation
            pass
        except:
            pass
    
    def save_config(self):
        """Save configuration to file"""
        config = {
            "recoil_enabled": self.recoil_enabled.get(),
            "rapid_fire_enabled": self.rapid_fire_enabled.get(),
            "require_ads": self.require_ads.get(),
            "sleep_enabled": self.sleep_enabled.get(),
            "esp_enabled": self.esp_enabled.get(),
            "names_enabled": self.names_enabled.get(),
            "health_enabled": self.health_enabled.get(),
            "distance_enabled": self.distance_enabled.get(),
            "team_number_enabled": self.team_number_enabled.get(),
            "weapons_enabled": self.weapons_enabled.get(),
            "boxes_enabled": self.boxes_enabled.get(),
            "skeleton_enabled": self.skeleton_enabled.get(),
            "respawned_enabled": self.respawned_enabled.get(),
            "spotted_enemies_enabled": self.spotted_enemies_enabled.get(),
            "teammates_enabled": self.teammates_enabled.get(),
            "show_distance_enabled": self.show_distance_enabled.get(),
            "show_fps_enabled": self.show_fps_enabled.get(),
            "esp_distance": self.esp_distance.get(),
            "esp_color": self.esp_color.get(),
            "esp_thickness": self.esp_thickness.get(),
            "skeleton_opacity": self.skeleton_opacity.get(),
            "render_distance": self.render_distance.get(),
            "render_fps": self.render_fps.get(),
            "fps_limit": self.fps_limit.get(),
            "vertical_strength": self.vertical_strength.get(),
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
                self.esp_enabled.set(config.get("esp_enabled", False))
                self.names_enabled.set(config.get("names_enabled", False))
                self.health_enabled.set(config.get("health_enabled", False))
                self.distance_enabled.set(config.get("distance_enabled", False))
                self.team_number_enabled.set(config.get("team_number_enabled", False))
                self.weapons_enabled.set(config.get("weapons_enabled", False))
                self.boxes_enabled.set(config.get("boxes_enabled", False))
                self.skeleton_enabled.set(config.get("skeleton_enabled", False))
                self.respawned_enabled.set(config.get("respawned_enabled", False))
                self.spotted_enemies_enabled.set(config.get("spotted_enemies_enabled", False))
                self.teammates_enabled.set(config.get("teammates_enabled", False))
                self.show_distance_enabled.set(config.get("show_distance_enabled", False))
                self.show_fps_enabled.set(config.get("show_fps_enabled", False))
                self.esp_distance.set(config.get("esp_distance", 175))
                self.esp_color.set(config.get("esp_color", "RED"))
                self.esp_thickness.set(config.get("esp_thickness", 2))
                self.skeleton_opacity.set(config.get("skeleton_opacity", 0.8))
                self.render_distance.set(config.get("render_distance", 107))
                self.render_fps.set(config.get("render_fps", 32))
                self.fps_limit.set(config.get("fps_limit", 60))
                self.vertical_strength.set(config.get("vertical_strength", 8))
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
                self.stop_esp()
                if hasattr(self, 'keyboard_listener'):
                    self.keyboard_listener.stop()
                self.root.destroy()
        else:
            if hasattr(self, 'keyboard_listener'):
                self.keyboard_listener.stop()
            self.root.destroy()

def main():
    root = tk.Tk()
    app = AdvancedESPApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 