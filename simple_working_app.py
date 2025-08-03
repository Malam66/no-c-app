import tkinter as tk
from tkinter import messagebox
import threading
import time
import keyboard as kb
import mouse as ms

class SimpleWorkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Simple Working No Recoil")
        self.root.geometry("400x500")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # App state
        self.app_running = False
        self.recoil_active = False
        
        # Variables
        self.recoil_enabled = tk.BooleanVar(value=False)
        self.vertical_strength = tk.IntVar(value=5)
        self.recoil_delay = tk.DoubleVar(value=0.02)
        
        # Threading
        self.recoil_thread = None
        self.running = False
        
        # Setup UI
        self.setup_ui()
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def setup_ui(self):
        """Setup the main user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#1a1a2e', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 SIMPLE NO RECOIL", 
                              font=('Arial', 18, 'bold'), 
                              fg='#ff6b6b', bg='#1a1a2e')
        title_label.pack(pady=(0, 20))
        
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
        self.status_indicator = tk.Label(toggle_frame, text="Click to start", 
                                        font=('Arial', 10), 
                                        fg='#4ecdc4', bg='#2a2a3e')
        self.status_indicator.pack(pady=(0, 10))
        
        # Recoil Section
        recoil_frame = tk.Frame(main_frame, bg='#2a2a3e', relief='raised', bd=2)
        recoil_frame.pack(fill='x', pady=10)
        
        # Title
        title_label = tk.Label(recoil_frame, text="🎯 RECOIL CONTROL", 
                              font=('Arial', 12, 'bold'), 
                              fg='#ff6b6b', bg='#2a2a3e')
        title_label.pack(pady=5)
        
        content_frame = tk.Frame(recoil_frame, bg='#2a2a3e', padx=10, pady=10)
        content_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        # Toggle recoil
        tk.Checkbutton(content_frame, text="🔫 ENABLE RECOIL CONTROL", 
                      variable=self.recoil_enabled, bg='#2a2a3e', fg='#ffffff',
                      selectcolor='#404050', activebackground='#2a2a3e',
                      activeforeground='#ffffff').pack(anchor='w', pady=2)
        
        # Vertical strength
        strength_frame = tk.Frame(content_frame, bg='#2a2a3e')
        strength_frame.pack(fill='x', pady=10)
        
        tk.Label(strength_frame, text="📈 VERTICAL STRENGTH:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        
        slider_frame = tk.Frame(strength_frame, bg='#2a2a3e')
        slider_frame.pack(fill='x', pady=2)
        
        slider = tk.Scale(slider_frame, from_=1, to=10,
                         variable=self.vertical_strength, orient='horizontal', 
                         bg='#2a2a3e', fg='#ffffff',
                         highlightbackground='#2a2a3e', troughcolor='#404050')
        slider.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        entry = tk.Entry(slider_frame, textvariable=self.vertical_strength, width=8, bg='#404050', fg='#ffffff')
        entry.pack(side='right')
        
        # Recoil delay
        delay_frame = tk.Frame(content_frame, bg='#2a2a3e')
        delay_frame.pack(fill='x', pady=10)
        
        tk.Label(delay_frame, text="⏱️ RECOIL DELAY:", bg='#2a2a3e', fg='#ffffff').pack(anchor='w')
        
        delay_slider_frame = tk.Frame(delay_frame, bg='#2a2a3e')
        delay_slider_frame.pack(fill='x', pady=2)
        
        delay_slider = tk.Scale(delay_slider_frame, from_=0.01, to=0.1, resolution=0.01,
                               variable=self.recoil_delay, orient='horizontal', 
                               bg='#2a2a3e', fg='#ffffff',
                               highlightbackground='#2a2a3e', troughcolor='#404050')
        delay_slider.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        delay_entry = tk.Entry(delay_slider_frame, textvariable=self.recoil_delay, width=8, bg='#404050', fg='#ffffff')
        delay_entry.pack(side='right')
        
        # Instructions
        info_frame = tk.Frame(main_frame, bg='#2a2a3e', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=10)
        
        info_label = tk.Label(info_frame, text="ℹ️ INSTRUCTIONS", 
                             font=('Arial', 12, 'bold'), 
                             fg='#4ecdc4', bg='#2a2a3e')
        info_label.pack(pady=5)
        
        info_content = tk.Frame(info_frame, bg='#2a2a3e', padx=10, pady=10)
        info_content.pack(fill='x', padx=10, pady=(0, 10))
        
        instructions = tk.Label(info_content, 
                              text="1. Click 'START' to activate\n2. Enable recoil control\n3. Go to your game\n4. Hold left mouse button to fire\n5. App will automatically compensate recoil",
                              font=('Arial', 10), 
                              fg='#cccccc', bg='#2a2a3e', justify='left')
        instructions.pack(anchor='w', pady=5)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener for hotkeys"""
        def on_press(key):
            try:
                if key == 'insert':
                    self.toggle_app()
            except:
                pass
        
        # Use keyboard library for hotkey
        kb.add_hotkey('insert', self.toggle_app)
        
    def toggle_app(self):
        """Toggle the application on/off"""
        if not self.app_running:
            self.app_running = True
            self.toggle_button.config(text="🟢 RUNNING", bg='#4ecdc4')
            self.status_indicator.config(text="App is running - Go to game", fg='#4ecdc4')
            messagebox.showinfo("Started", "App is now running!\nGo to your game and hold left mouse button.\nPress INSERT to stop.")
        else:
            self.app_running = False
            self.toggle_button.config(text="🔴 STOPPED", bg='#ff6b6b')
            self.status_indicator.config(text="App stopped", fg='#ff6b6b')
            self.stop_recoil()
            messagebox.showinfo("Stopped", "App has been stopped.")
    
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
    
    def recoil_loop(self):
        """Simple recoil control loop"""
        while self.running:
            if self.recoil_enabled.get() and self.app_running:
                # Check if left mouse button is pressed
                if kb.is_pressed('left'):
                    # Get current settings
                    vertical = self.vertical_strength.get()
                    delay = self.recoil_delay.get()
                    
                    # Move mouse down to compensate recoil
                    ms.move(0, vertical, absolute=False)
                    time.sleep(delay)
            time.sleep(0.01)
    
    def on_closing(self):
        """Handle application closing"""
        if self.app_running:
            if messagebox.askokcancel("Quit", "App is running. Do you want to quit?"):
                self.stop_recoil()
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = SimpleWorkingApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 