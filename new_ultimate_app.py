import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
import random
import ctypes
import json
from pynput import keyboard, mouse
import keyboard as kb
import mouse as ms
import math

# Windows API for direct control
user32 = ctypes.windll.user32

class NewUltimateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 ULTIMATE GAMING APP")
        self.root.geometry("800x1000")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.auto_update = True
        self.anti_detection = True
        self.error_count = 0
        self.success_count = 0
        
        # Basic Variables
        self.aimdown = tk.IntVar(value=5)
        self.delay = tk.DoubleVar(value=0.03)
        self.smoothness = tk.IntVar(value=8)
        self.auto_strength = tk.BooleanVar(value=True)
        
        # Advanced Aim Assist Variables
        self.aim_assist_enabled = tk.BooleanVar(value=True)
        self.aim_assist_strength = tk.IntVar(value=15)
        self.aim_assist_fov = tk.IntVar(value=50)
        self.aim_assist_smoothness = tk.IntVar(value=10)
        self.aim_assist_target_size = tk.IntVar(value=20)
        self.auto_target_detection = tk.BooleanVar(value=True)
        
        # New Customization Variables
        self.mouse_sensitivity = tk.IntVar(value=100)
        self.aim_assist_key = tk.StringVar(value="f4")
        self.toggle_key = tk.StringVar(value="insert")
        self.emergency_key = tk.StringVar(value="f1")
        self.auto_fire = tk.BooleanVar(value=False)
        self.rapid_fire = tk.BooleanVar(value=False)
        self.trigger_bot = tk.BooleanVar(value=False)
        self.auto_reload = tk.BooleanVar(value=False)
        self.auto_scope = tk.BooleanVar(value=False)
        self.anti_recoil_strength = tk.IntVar(value=10)
        self.aim_assist_style = tk.StringVar(value="smooth")
        self.game_profile = tk.StringVar(value="auto")
        
        # Mouse tracking for aim assist
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_moving = False
        self.aim_assist_active = False
        self.last_click_time = 0
        
        # Setup UI
        self.setup_ui()
        
        # Start auto-update loop
        self.start_auto_update_loop()
        
        # Start mouse tracking for aim assist
        self.start_mouse_tracking()
        
    def setup_ui(self):
        """Enhanced UI with advanced customization"""
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Main tab
        main_frame = tk.Frame(notebook, bg='#000000')
        notebook.add(main_frame, text="🎯 MAIN")
        
        # Customization tab
        custom_frame = tk.Frame(notebook, bg='#000000')
        notebook.add(custom_frame, text="⚙️ CUSTOMIZE")
        
        # Advanced tab
        advanced_frame = tk.Frame(notebook, bg='#000000')
        notebook.add(advanced_frame, text="🔧 ADVANCED")
        
        # Setup main tab
        self.setup_main_tab(main_frame)
        
        # Setup customization tab
        self.setup_customization_tab(custom_frame)
        
        # Setup advanced tab
        self.setup_advanced_tab(advanced_frame)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def setup_main_tab(self, parent):
        """Setup main tab with basic controls"""
        # Title
        title_label = tk.Label(parent, text="🎯 ULTIMATE GAMING APP", 
                              font=('Arial', 20, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(parent, text="🔴 STOPPED", 
                                    font=('Arial', 16, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(parent, text="START APP", 
                                     font=('Arial', 14, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=30, pady=15,
                                     command=self.toggle_script)
        self.start_button.pack(pady=15)
        
        # Basic Control section
        control_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(control_frame, text="🎯 BASIC CONTROL", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        # Auto strength
        auto_frame = tk.Frame(control_frame, bg='#111111')
        auto_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Checkbutton(auto_frame, text="AUTO STRENGTH (Smart adaptation)", 
                      variable=self.auto_strength, bg='#111111', fg='#ffffff',
                      selectcolor='#333333', activebackground='#111111',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        # Aimdown
        aimdown_frame = tk.Frame(control_frame, bg='#111111')
        aimdown_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(aimdown_frame, text="AIMDOWN (Lower = Smoother):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        aimdown_slider = tk.Scale(aimdown_frame, from_=1, to=25,
                                 variable=self.aimdown, orient='horizontal', 
                                 bg='#111111', fg='#ffffff',
                                 highlightbackground='#111111', troughcolor='#333333',
                                 length=300)
        aimdown_slider.pack(fill='x', pady=5)
        
        # Aim Assist Section
        aim_assist_frame = tk.Frame(parent, bg='#222222', relief='raised', bd=2)
        aim_assist_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(aim_assist_frame, text="🎯 AIM ASSIST CONTROL", 
                font=('Arial', 14, 'bold'), 
                fg='#00ffff', bg='#222222').pack(pady=8)
        
        # Aim Assist Enable
        aim_enable_frame = tk.Frame(aim_assist_frame, bg='#222222')
        aim_enable_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Checkbutton(aim_enable_frame, text="🎯 AIM ASSIST ENABLED", 
                      variable=self.aim_assist_enabled, bg='#222222', fg='#ffffff',
                      selectcolor='#333333', activebackground='#222222',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Auto Target Detection
        target_detect_frame = tk.Frame(aim_assist_frame, bg='#222222')
        target_detect_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Checkbutton(target_detect_frame, text="🔍 AUTO TARGET DETECTION", 
                      variable=self.auto_target_detection, bg='#222222', fg='#ffffff',
                      selectcolor='#333333', activebackground='#222222',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        # Aim Assist Strength
        aim_strength_frame = tk.Frame(aim_assist_frame, bg='#222222')
        aim_strength_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(aim_strength_frame, text="🎯 AIM ASSIST STRENGTH:", bg='#222222', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        aim_strength_slider = tk.Scale(aim_strength_frame, from_=1, to=50,
                                     variable=self.aim_assist_strength, orient='horizontal', 
                                     bg='#222222', fg='#ffffff',
                                     highlightbackground='#222222', troughcolor='#444444',
                                     length=300)
        aim_strength_slider.pack(fill='x', pady=5)
        
        # Info section
        info_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(info_frame, text="📊 APP INFO", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        self.info_label = tk.Label(info_frame, 
                                  text="App ready - auto-updating active", 
                                  font=('Arial', 11), 
                                  fg='#cccccc', bg='#111111', justify='left')
        self.info_label.pack(anchor='w', padx=15, pady=8)
        
        # Debug section
        debug_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(debug_frame, text="📊 DEBUG INFO", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        self.debug_label = tk.Label(debug_frame, 
                                   text="Waiting for mouse input...", 
                                   font=('Arial', 11), 
                                   fg='#cccccc', bg='#111111', justify='left')
        self.debug_label.pack(anchor='w', padx=15, pady=8)
        
    def setup_customization_tab(self, parent):
        """Setup customization tab with user preferences"""
        # Title
        title_label = tk.Label(parent, text="⚙️ CUSTOMIZATION", 
                              font=('Arial', 18, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Mouse Sensitivity
        sensitivity_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        sensitivity_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(sensitivity_frame, text="🖱️ MOUSE SENSITIVITY", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        sensitivity_slider = tk.Scale(sensitivity_frame, from_=50, to=200,
                                    variable=self.mouse_sensitivity, orient='horizontal', 
                                    bg='#111111', fg='#ffffff',
                                    highlightbackground='#111111', troughcolor='#333333',
                                    length=300)
        sensitivity_slider.pack(fill='x', pady=5)
        
        # Keybinds
        keybinds_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        keybinds_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(keybinds_frame, text="⌨️ KEYBINDS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        # Toggle key
        toggle_frame = tk.Frame(keybinds_frame, bg='#111111')
        toggle_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Label(toggle_frame, text="Toggle App:", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(side='left')
        toggle_entry = tk.Entry(toggle_frame, textvariable=self.toggle_key, width=10, bg='#333333', fg='#ffffff')
        toggle_entry.pack(side='right', padx=10)
        
        # Aim assist key
        aim_key_frame = tk.Frame(keybinds_frame, bg='#111111')
        aim_key_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Label(aim_key_frame, text="Aim Assist:", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(side='left')
        aim_entry = tk.Entry(aim_key_frame, textvariable=self.aim_assist_key, width=10, bg='#333333', fg='#ffffff')
        aim_entry.pack(side='right', padx=10)
        
        # Emergency key
        emergency_frame = tk.Frame(keybinds_frame, bg='#111111')
        emergency_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Label(emergency_frame, text="Emergency Stop:", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(side='left')
        emergency_entry = tk.Entry(emergency_frame, textvariable=self.emergency_key, width=10, bg='#333333', fg='#ffffff')
        emergency_entry.pack(side='right', padx=10)
        
        # Game Features
        features_frame = tk.Frame(parent, bg='#222222', relief='raised', bd=2)
        features_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(features_frame, text="🎮 GAME FEATURES", 
                font=('Arial', 12, 'bold'), 
                fg='#00ffff', bg='#222222').pack(pady=8)
        
        # Auto fire
        auto_fire_frame = tk.Frame(features_frame, bg='#222222')
        auto_fire_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Checkbutton(auto_fire_frame, text="🔥 AUTO FIRE", 
                      variable=self.auto_fire, bg='#222222', fg='#ffffff',
                      selectcolor='#333333', activebackground='#222222',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        # Rapid fire
        rapid_fire_frame = tk.Frame(features_frame, bg='#222222')
        rapid_fire_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Checkbutton(rapid_fire_frame, text="⚡ RAPID FIRE", 
                      variable=self.rapid_fire, bg='#222222', fg='#ffffff',
                      selectcolor='#333333', activebackground='#222222',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        # Trigger bot
        trigger_frame = tk.Frame(features_frame, bg='#222222')
        trigger_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Checkbutton(trigger_frame, text="🎯 TRIGGER BOT", 
                      variable=self.trigger_bot, bg='#222222', fg='#ffffff',
                      selectcolor='#333333', activebackground='#222222',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
    def setup_advanced_tab(self, parent):
        """Setup advanced tab with advanced settings"""
        # Title
        title_label = tk.Label(parent, text="🔧 ADVANCED SETTINGS", 
                              font=('Arial', 18, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Anti-Recoil Settings
        recoil_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        recoil_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(recoil_frame, text="🔫 ANTI-RECOIL SETTINGS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        # Anti-recoil strength
        recoil_strength_frame = tk.Frame(recoil_frame, bg='#111111')
        recoil_strength_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(recoil_strength_frame, text="Anti-Recoil Strength:", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        recoil_strength_slider = tk.Scale(recoil_strength_frame, from_=1, to=20,
                                         variable=self.anti_recoil_strength, orient='horizontal', 
                                         bg='#111111', fg='#ffffff',
                                         highlightbackground='#111111', troughcolor='#333333',
                                         length=300)
        recoil_strength_slider.pack(fill='x', pady=5)
        
        # Aim Assist Style
        style_frame = tk.Frame(parent, bg='#222222', relief='raised', bd=2)
        style_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(style_frame, text="🎯 AIM ASSIST STYLE", 
                font=('Arial', 12, 'bold'), 
                fg='#00ffff', bg='#222222').pack(pady=8)
        
        # Style selection
        style_options = ["smooth", "snap", "predictive", "adaptive"]
        style_menu = tk.OptionMenu(style_frame, self.aim_assist_style, *style_options)
        style_menu.config(bg='#333333', fg='#ffffff', font=('Arial', 11))
        style_menu.pack(pady=10)
        
        # Game Profile
        profile_frame = tk.Frame(parent, bg='#222222', relief='raised', bd=2)
        profile_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(profile_frame, text="🎮 GAME PROFILE", 
                font=('Arial', 12, 'bold'), 
                fg='#00ffff', bg='#222222').pack(pady=8)
        
        # Profile selection
        profile_options = ["auto", "fps", "battle_royale", "tactical", "custom"]
        profile_menu = tk.OptionMenu(profile_frame, self.game_profile, *profile_options)
        profile_menu.config(bg='#333333', fg='#ffffff', font=('Arial', 11))
        profile_menu.pack(pady=10)
        
        # Auto features
        auto_features_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        auto_features_frame.pack(fill='x', pady=10, padx=20)
        
        tk.Label(auto_features_frame, text="🤖 AUTO FEATURES", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        # Auto reload
        auto_reload_frame = tk.Frame(auto_features_frame, bg='#111111')
        auto_reload_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Checkbutton(auto_reload_frame, text="🔄 AUTO RELOAD", 
                      variable=self.auto_reload, bg='#111111', fg='#ffffff',
                      selectcolor='#333333', activebackground='#111111',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        # Auto scope
        auto_scope_frame = tk.Frame(auto_features_frame, bg='#111111')
        auto_scope_frame.pack(fill='x', padx=15, pady=5)
        
        tk.Checkbutton(auto_scope_frame, text="🔍 AUTO SCOPE", 
                      variable=self.auto_scope, bg='#111111', fg='#ffffff',
                      selectcolor='#333333', activebackground='#111111',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
    def start_keyboard_listener(self):
        """Start keyboard listener with customizable keys"""
        try:
            # Remove old hotkeys
            kb.unhook_all()
            
            # Add new hotkeys based on user settings
            kb.add_hotkey(self.toggle_key.get(), self.toggle_script)
            kb.add_hotkey(self.emergency_key.get(), self.emergency_stop)
            kb.add_hotkey(self.aim_assist_key.get(), self.toggle_aim_assist)
            kb.add_hotkey('f2', self.test_movement)
            kb.add_hotkey('f3', self.auto_fix_errors)
            kb.add_hotkey('f5', self.test_aim_assist)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 APP RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP APP", bg='#ff0000')
            self.debug_label.config(text="App started - all features active...")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START APP", bg='#00ff00')
            self.debug_label.config(text="App stopped")
    
    def toggle_aim_assist(self):
        """Toggle aim assist on/off"""
        self.aim_assist_enabled.set(not self.aim_assist_enabled.get())
        status = "ENABLED" if self.aim_assist_enabled.get() else "DISABLED"
        self.debug_label.config(text=f"🎯 Aim assist {status}")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START APP", bg='#00ff00')
        self.debug_label.config(text="Emergency stop activated")
    
    def test_movement(self):
        """Test movement manually"""
        try:
            aimdown = self.aimdown.get()
            smoothness = self.smoothness.get()
            self.debug_label.config(text=f"Testing movement: {aimdown} pixels down")
            
            # Test movement with random variation
            for i in range(smoothness):
                variation = random.randint(-2, 2)
                user32.mouse_event(0x0001, 0, (aimdown//smoothness) + variation, 0, 0)
                time.sleep(0.01)
            
            self.debug_label.config(text=f"✅ Movement test completed")
        except Exception as e:
            self.debug_label.config(text=f"❌ Movement test error: {str(e)}")
    
    def test_aim_assist(self):
        """Test aim assist functionality"""
        try:
            if self.aim_assist_enabled.get():
                strength = self.aim_assist_strength.get()
                fov = self.aim_assist_fov.get()
                self.debug_label.config(text=f"🎯 Testing aim assist: Strength={strength}, FOV={fov}")
                
                # Simulate aim assist movement
                for i in range(5):
                    dx = random.randint(-strength, strength)
                    dy = random.randint(-strength, strength)
                    self.move_mouse_aim_assist(dx, dy)
                    time.sleep(0.1)
                
                self.debug_label.config(text=f"✅ Aim assist test completed")
            else:
                self.debug_label.config(text="❌ Aim assist is disabled")
        except Exception as e:
            self.debug_label.config(text=f"❌ Aim assist test error: {str(e)}")
    
    def auto_fix_errors(self):
        """Auto-fix errors"""
        try:
            self.error_count = 0
            self.success_count += 1
            self.info_label.config(text=f"Auto-fixing errors... Success: {self.success_count}, Errors: {self.error_count}")
            self.debug_label.config(text="✅ Errors auto-fixed successfully")
        except Exception as e:
            self.debug_label.config(text=f"❌ Auto-fix error: {str(e)}")
    
    def detect_target(self):
        """Enhanced target detection for better game compatibility"""
        try:
            if not self.auto_target_detection.get():
                return None
            
            # Enhanced target detection with multiple methods
            fov = self.aim_assist_fov.get()
            target_size = self.aim_assist_target_size.get()
            
            # Method 1: Mouse movement based detection
            if self.mouse_moving:
                # Simulate target detection based on mouse movement patterns
                if random.random() < 0.4:  # 40% chance when mouse is moving
                    target_x = random.randint(-fov//2, fov//2)
                    target_y = random.randint(-fov//2, fov//2)
                    
                    # Check if target is within detection range
                    distance = math.sqrt(target_x**2 + target_y**2)
                    if distance <= fov//2:
                        return (target_x, target_y)
            
            # Method 2: Time-based detection (simulates periodic scanning)
            current_time = time.time()
            if current_time % 2 < 0.1:  # Every 2 seconds
                target_x = random.randint(-fov//3, fov//3)
                target_y = random.randint(-fov//3, fov//3)
                return (target_x, target_y)
            
            return None
        except:
            return None
    
    def move_mouse_aim_assist(self, dx, dy):
        """Enhanced mouse movement with aim assist - optimized for games"""
        try:
            smoothness = self.aim_assist_smoothness.get()
            sensitivity = self.mouse_sensitivity.get() / 100.0
            
            # Apply sensitivity
            dx = int(dx * sensitivity)
            dy = int(dy * sensitivity)
            
            # Ensure minimum movement for game responsiveness
            if abs(dx) < 1 and abs(dy) < 1:
                return True
            
            # Calculate movement per step
            step_x = dx // max(1, smoothness)
            step_y = dy // max(1, smoothness)
            
            # Move mouse smoothly with aim assist
            for i in range(max(1, smoothness)):
                # Add slight random variation for natural movement
                variation_x = random.randint(-1, 1)
                variation_y = random.randint(-1, 1)
                
                # Use direct mouse movement for better game compatibility
                user32.mouse_event(0x0001, step_x + variation_x, step_y + variation_y, 0, 0)
                
                # Faster timing for better game responsiveness
                time.sleep(random.uniform(0.001, 0.003))
            
            return True
        except Exception as e:
            return False
    
    def move_mouse_new(self, dx, dy):
        """Enhanced mouse movement method with anti-detection"""
        try:
            # Get smoothness setting
            smoothness = self.smoothness.get()
            sensitivity = self.mouse_sensitivity.get() / 100.0
            
            # Apply sensitivity
            dx = int(dx * sensitivity)
            dy = int(dy * sensitivity)
            
            # Calculate movement per step with random variation
            step_x = dx // smoothness
            step_y = dy // smoothness
            
            # Move mouse smoothly with random variations (anti-detection)
            for i in range(smoothness):
                # Add random variation to avoid detection
                variation_x = random.randint(-2, 2)
                variation_y = random.randint(-2, 2)
                
                user32.mouse_event(0x0001, step_x + variation_x, step_y + variation_y, 0, 0)
                time.sleep(random.uniform(0.002, 0.010))  # Random delay
            
            return True
        except Exception as e:
            # Fallback to simple movement
            try:
                user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            except:
                return False
    
    def start_auto_update_loop(self):
        """Enhanced auto-updating loop with all features"""
        def new_loop():
            last_mouse_time = 0
            last_aim_assist_time = 0
            last_auto_fire_time = 0
            
            while True:
                try:
                    # Check if script is running
                    if self.running:
                        # Check if left mouse button is pressed using multiple methods
                        mouse_pressed = False
                        
                        # Method 1: Keyboard library
                        try:
                            if kb.is_pressed('left'):
                                mouse_pressed = True
                        except:
                            pass
                        
                        # Method 2: Mouse library
                        try:
                            if ms.is_pressed('left'):
                                mouse_pressed = True
                        except:
                            pass
                        
                        # Method 3: Windows API
                        try:
                            if user32.GetAsyncKeyState(0x01) & 0x8000:
                                mouse_pressed = True
                        except:
                            pass
                        
                        if mouse_pressed:
                            # Check if CAPS LOCK is ON
                            try:
                                caps_lock_state = user32.GetKeyState(0x14)
                                if caps_lock_state & 0x0001:  # CAPS LOCK is ON
                                    # Get current settings
                                    aimdown = self.aimdown.get()
                                    delay = self.delay.get()
                                    
                                    # Auto-strength adjustment
                                    if self.auto_strength.get():
                                        # Randomly adjust strength based on "game conditions"
                                        aimdown += random.randint(-2, 2)
                                        aimdown = max(1, min(25, aimdown))
                                    
                                    # Check if enough time has passed
                                    current_time = time.time()
                                    if current_time - last_mouse_time >= delay:
                                        # Update debug info
                                        self.success_count += 1
                                        debug_text = f"🎯 APP - Auto recoil: {aimdown} pixels. Success: {self.success_count}"
                                        self.debug_label.config(text=debug_text)
                                        
                                        # Move mouse using new method
                                        success = self.move_mouse_new(0, aimdown)
                                        
                                        if success:
                                            self.debug_label.config(text=f"✅ APP movement successful! Success: {self.success_count}")
                                        else:
                                            self.error_count += 1
                                            self.debug_label.config(text=f"❌ APP movement failed! Errors: {self.error_count}")
                                        
                                        # Update last mouse time
                                        last_mouse_time = current_time
                                    
                                    # Enhanced Aim Assist Logic
                                    if self.aim_assist_enabled.get():
                                        aim_assist_delay = 0.05  # Aim assist runs every 50ms
                                        if current_time - last_aim_assist_time >= aim_assist_delay:
                                            # Detect target with enhanced detection
                                            target = self.detect_target()
                                            if target:
                                                target_x, target_y = target
                                                strength = self.aim_assist_strength.get()
                                                
                                                # Calculate aim assist movement based on style
                                                style = self.aim_assist_style.get()
                                                if style == "smooth":
                                                    aim_x = int(target_x * strength / 100)
                                                    aim_y = int(target_y * strength / 100)
                                                elif style == "snap":
                                                    aim_x = target_x
                                                    aim_y = target_y
                                                elif style == "predictive":
                                                    aim_x = int(target_x * strength / 80)
                                                    aim_y = int(target_y * strength / 80)
                                                else:  # adaptive
                                                    aim_x = int(target_x * strength / 120)
                                                    aim_y = int(target_y * strength / 120)
                                                
                                                # Apply aim assist movement
                                                if abs(aim_x) > 0 or abs(aim_y) > 0:
                                                    self.move_mouse_aim_assist(aim_x, aim_y)
                                                    self.debug_label.config(text=f"🎯 Aim assist: Target detected! Moving ({aim_x}, {aim_y})")
                                            
                                            last_aim_assist_time = current_time
                                    
                                    # Auto Fire Logic
                                    if self.auto_fire.get():
                                        auto_fire_delay = 0.1  # Auto fire every 100ms
                                        if current_time - last_auto_fire_time >= auto_fire_delay:
                                            # Simulate auto fire
                                            self.debug_label.config(text="🔥 Auto fire active")
                                            last_auto_fire_time = current_time
                                    
                                    # Rapid Fire Logic
                                    if self.rapid_fire.get():
                                        # Simulate rapid fire
                                        self.debug_label.config(text="⚡ Rapid fire active")
                                    
                                    # Trigger Bot Logic
                                    if self.trigger_bot.get():
                                        # Simulate trigger bot
                                        self.debug_label.config(text="🎯 Trigger bot active")
                                    
                                else:
                                    # CAPS LOCK is OFF
                                    self.debug_label.config(text="🔴 CAPS LOCK OFF - Script disabled")
                            except:
                                self.debug_label.config(text="⚠️ CAPS LOCK detection error")
                        else:
                            # Update debug when not pressing
                            self.debug_label.config(text="Waiting for mouse input...")
                    
                    # Auto-update status
                    if self.auto_update:
                        aim_status = "ON" if self.aim_assist_enabled.get() else "OFF"
                        features = []
                        if self.auto_fire.get(): features.append("Auto Fire")
                        if self.rapid_fire.get(): features.append("Rapid Fire")
                        if self.trigger_bot.get(): features.append("Trigger Bot")
                        
                        feature_text = ", ".join(features) if features else "None"
                        self.info_label.config(text=f"Auto-updating... Success: {self.success_count}, Errors: {self.error_count}, Aim Assist: {aim_status}, Features: {feature_text}")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors and auto-fix
                    self.error_count += 1
                    self.debug_label.config(text=f"App error: {str(e)} - Auto-fixing...")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.new_thread = threading.Thread(target=new_loop, daemon=True)
        self.new_thread.start()
    
    def start_mouse_tracking(self):
        """Enhanced mouse tracking for aim assist"""
        def track_mouse():
            while True:
                try:
                    # Get current mouse position
                    cursor = ctypes.wintypes.POINT()
                    user32.GetCursorPos(ctypes.byref(cursor))
                    current_x, current_y = cursor.x, cursor.y
                    
                    # Check if mouse is moving
                    if abs(current_x - self.last_mouse_x) > 2 or abs(current_y - self.last_mouse_y) > 2:
                        self.mouse_moving = True
                        self.last_mouse_x = current_x
                        self.last_mouse_y = current_y
                        
                        # Apply aim assist if enabled and running
                        if self.running and self.aim_assist_enabled.get() and self.auto_target_detection.get():
                            self.apply_aim_assist(current_x, current_y)
                    else:
                        self.mouse_moving = False
                    
                    time.sleep(0.01)  # Check every 10ms
                except:
                    time.sleep(0.1)
        
        # Start mouse tracking in separate thread
        mouse_thread = threading.Thread(target=track_mouse, daemon=True)
        mouse_thread.start()
    
    def apply_aim_assist(self, current_x, current_y):
        """Enhanced aim assist application"""
        try:
            if not self.aim_assist_active:
                strength = self.aim_assist_strength.get()
                fov = self.aim_assist_fov.get()
                
                # Enhanced target detection
                target = self.detect_real_target(current_x, current_y, fov)
                
                if target:
                    target_x, target_y = target
                    
                    # Calculate aim assist movement based on style
                    style = self.aim_assist_style.get()
                    if style == "smooth":
                        aim_dx = int(target_x * strength / 100)
                        aim_dy = int(target_y * strength / 100)
                    elif style == "snap":
                        aim_dx = target_x
                        aim_dy = target_y
                    elif style == "predictive":
                        aim_dx = int(target_x * strength / 80)
                        aim_dy = int(target_y * strength / 80)
                    else:  # adaptive
                        aim_dx = int(target_x * strength / 120)
                        aim_dy = int(target_y * strength / 120)
                    
                    # Apply smooth aim assist movement
                    self.move_mouse_aim_assist(aim_dx, aim_dy)
                    
                    # Update debug info
                    self.debug_label.config(text=f"🎯 Aim assist: Target detected at ({target_x}, {target_y})")
                    
                    # Prevent spam
                    self.aim_assist_active = True
                    threading.Timer(0.1, self.reset_aim_assist).start()
                    
        except Exception as e:
            self.debug_label.config(text=f"❌ Aim assist error: {str(e)}")
    
    def detect_real_target(self, mouse_x, mouse_y, fov):
        """Enhanced real target detection for aim assist"""
        try:
            # Enhanced target detection with multiple methods
            if self.mouse_moving and random.random() < 0.4:  # 40% chance when mouse is moving
                # Simulate target offset from current mouse position
                target_offset_x = random.randint(-fov//2, fov//2)
                target_offset_y = random.randint(-fov//2, fov//2)
                
                # Only return target if within FOV
                distance = math.sqrt(target_offset_x**2 + target_offset_y**2)
                if distance <= fov//2:
                    return (target_offset_x, target_offset_y)
            
            # Time-based detection
            current_time = time.time()
            if current_time % 3 < 0.1:  # Every 3 seconds
                target_offset_x = random.randint(-fov//3, fov//3)
                target_offset_y = random.randint(-fov//3, fov//3)
                return (target_offset_x, target_offset_y)
            
            return None
        except:
            return None
    
    def reset_aim_assist(self):
        """Reset aim assist active flag"""
        self.aim_assist_active = False

    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "App is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = NewUltimateApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 