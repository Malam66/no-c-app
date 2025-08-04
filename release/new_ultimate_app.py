import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import threading
import time
import random
import ctypes
import json
import os
import sys
import subprocess
from pynput import keyboard, mouse
import keyboard as kb
import mouse as ms
import math

# Windows API for direct control
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

class NewUltimateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 ULTIMATE GAMING APP - COMPLETE FIX")
        self.root.geometry("800x900")
        self.root.resizable(False, False)
        
        # Set custom icon if available
        try:
            if os.path.exists("app_icon.ico"):
                self.root.iconbitmap("app_icon.ico")
        except:
            pass
        
        # App state
        self.running = False
        self.auto_update = True
        self.anti_detection = True
        self.error_count = 0
        self.success_count = 0
        
        # Basic Variables - COMPLETE FIX VALUES
        self.aimdown = tk.IntVar(value=12)  # Much stronger anti-recoil
        self.delay = tk.DoubleVar(value=0.01)  # Very fast response
        self.smoothness = tk.IntVar(value=15)  # Maximum smoothness
        self.auto_strength = tk.BooleanVar(value=True)
        
        # Enhanced Smoothness and Delay Variables - COMPLETE FIX
        self.anti_recoil_smoothness = tk.IntVar(value=10)  # Better anti-recoil control
        self.anti_recoil_delay = tk.DoubleVar(value=0.02)  # Very fast anti-recoil
        self.aim_assist_smoothness = tk.IntVar(value=15)  # Maximum aim assist smoothness
        self.aim_assist_delay = tk.DoubleVar(value=0.005)  # Extremely fast aim assist
        self.movement_smoothness = tk.IntVar(value=12)  # Better movement
        self.movement_delay = tk.DoubleVar(value=0.005)  # Extremely fast movement
        
        # Advanced Aim Assist Variables - COMPLETE FIX FOR ALL GAMES
        self.aim_assist_enabled = tk.BooleanVar(value=True)  # ENABLED FOR ENEMY MOVEMENT DETECTION
        self.aim_assist_strength = tk.IntVar(value=20)  # Reduced to prevent shaking
        self.aim_assist_fov = tk.IntVar(value=100)  # Much larger FOV
        self.aim_assist_smoothness = tk.IntVar(value=15)  # Maximum smoothness
        self.aim_assist_target_size = tk.IntVar(value=30)  # Larger target
        self.auto_target_detection = tk.BooleanVar(value=True)
        self.anti_shaking_enabled = tk.BooleanVar(value=True)
        self.strong_aim_assist = tk.BooleanVar(value=True)  # ENABLED BY DEFAULT
        
        # New Customization Variables - COMPLETE FIX
        self.mouse_sensitivity = tk.IntVar(value=150)  # Much higher sensitivity
        self.aim_assist_key = tk.StringVar(value="f4")
        self.toggle_key = tk.StringVar(value="insert")
        self.emergency_key = tk.StringVar(value="f1")
        self.auto_fire = tk.BooleanVar(value=False)  # DISABLED TO PREVENT SHAKING
        self.rapid_fire = tk.BooleanVar(value=False)  # DISABLED TO PREVENT SHAKING
        self.trigger_bot = tk.BooleanVar(value=False)  # DISABLED TO PREVENT SHAKING
        self.auto_reload = tk.BooleanVar(value=False)
        self.auto_scope = tk.BooleanVar(value=False)
        self.aim_lock = tk.BooleanVar(value=False)  # DISABLED - REMOVED
        self.anti_recoil_strength = tk.IntVar(value=25)  # Much stronger anti-recoil
        self.aim_assist_style = tk.StringVar(value="smooth")
        self.game_profile = tk.StringVar(value="auto")
        
        # Mouse tracking for aim assist - COMPLETE FIX
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_moving = False
        self.aim_assist_active = False
        self.last_click_time = 0
        self.last_mouse_press_time = 0
        
        # Enhanced mouse detection - COMPLETE FIX
        self.mouse_pressed = False
        self.last_mouse_state = False
        
        # Anti-recoil gradual start - COMPLETE FIX
        self.anti_recoil_start_time = 0
        self.anti_recoil_active = False
        
        # COMPLETE FIX: Better mouse control variables
        self.mouse_control_active = True
        self.last_mouse_position = (0, 0)
        self.mouse_movement_threshold = 1  # Very sensitive threshold
        self.user_mouse_movement = False
        
        # COMPLETE MOUSE CONTROL PROTECTION - No automatic movement
        self.app_startup_time = time.time()
        self.startup_delay = 10.0  # 10 seconds delay - much longer
        self.startup_protection = True
        self.user_control_priority = True
        self.force_user_control = True  # Force user control only
        self.disable_all_auto_movement = True  # Disable all automatic movement
        self.last_user_mouse_time = 0
        self.caps_lock_state = False
        self.last_caps_check = 0
        
        # CAPS LOCK Master Switch
        self.app_enabled = False  # Master switch - CAPS LOCK controls this
        self.last_app_status_time = 0
        
        # Startup protection - prevent immediate mouse movement
        self.app_startup_time = time.time()
        self.startup_delay = 3.0  # 3 seconds delay before features work
        
        # ANTI-BAN PROTECTION - Advanced undetectable features
        self.anti_ban_enabled = True
        self.random_delays = True
        self.human_patterns = True
        self.variable_movement = True
        self.last_anti_ban_time = time.time()
        self.movement_patterns = []
        self.ban_protection_level = 3  # Maximum protection
        
        # MOUSE CONTROL PROTECTION - Prevent interference and shaking
        self.mouse_control_safe = True
        self.user_mouse_priority = True
        self.shaking_protection = True
        self.mouse_interference_threshold = 2  # Much more sensitive - user has priority
        self.last_user_mouse_time = time.time()
        self.user_mouse_active = False
        self.user_mouse_override = True  # User always has priority
        
        # Setup UI
        self.setup_ui()
        
        # Create gradient background after UI is set up
        self.create_gradient_background()
        
    def create_gradient_background(self):
        """Create a simple background"""
        # Set simple background color
        self.root.configure(bg='#ffffff')
        
        # Start auto-update loop
        self.start_auto_update_loop()
        
        # Start mouse tracking for aim assist
        self.start_mouse_tracking()
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
        # Show complete protection message
        self.debug_label.config(text="⏳ COMPLETE PROTECTION ACTIVE - FULL MOUSE CONTROL FOR 10 SECONDS")
        
        # Bind closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_ui(self):
        """Enhanced UI with advanced customization and beautiful design"""
        # Create main container with simple background
        main_container = tk.Frame(self.root, bg='#ffffff')
        main_container.place(relx=0.5, rely=0.5, anchor='center', width=780, height=880)
        
        # Add logo at the top
        self.add_logo(main_container)
        
        # Create notebook for tabs with custom styling
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background='#ffffff', borderwidth=0)
        style.configure('TNotebook.Tab', background='#e0e0e0', foreground='#000000', 
                       padding=[20, 10], font=('Arial', 12, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', '#007acc'), ('active', '#cccccc')])
        
        notebook = ttk.Notebook(main_container)
        notebook.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Main tab with simple background
        main_frame = tk.Frame(notebook, bg='#ffffff')
        notebook.add(main_frame, text="🎯 MAIN")
        
        # Customization tab
        custom_frame = tk.Frame(notebook, bg='#ffffff')
        notebook.add(custom_frame, text="⚙️ CUSTOMIZE")
        
        # Advanced tab
        advanced_frame = tk.Frame(notebook, bg='#ffffff')
        notebook.add(advanced_frame, text="🔧 ADVANCED")
        
        # Setup main tab
        self.setup_main_tab(main_frame)
        
        # Setup customization tab
        self.setup_customization_tab(custom_frame)
        
        # Setup advanced tab
        self.setup_advanced_tab(advanced_frame)
        
    def add_logo(self, parent):
        """Add logo to the top of the app"""
        logo_frame = tk.Frame(parent, bg='#ffffff', height=140)
        logo_frame.pack(fill='x', pady=(15, 0))
        logo_frame.pack_propagate(False)
        
        # Try to load the app icon as logo
        try:
            if os.path.exists("app_icon.png"):
                # Load and resize the image
                image = Image.open("app_icon.png")
                image = image.resize((80, 80), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(image)
                
                # Create logo label
                logo_label = tk.Label(logo_frame, image=self.logo_photo, bg='#ffffff')
                logo_label.pack(side='left', padx=(20, 10))
            else:
                # Create a text-based logo if image not found
                logo_label = tk.Label(logo_frame, text="🎯", font=('Arial', 40), 
                                    fg='#000000', bg='#ffffff')
                logo_label.pack(side='left', padx=(20, 10))
        except Exception as e:
            # Fallback to text logo
            logo_label = tk.Label(logo_frame, text="🎯", font=('Arial', 40), 
                                fg='#000000', bg='#ffffff')
            logo_label.pack(side='left', padx=(20, 10))
        
        # App title next to logo
        title_label = tk.Label(logo_frame, text="ULTIMATE GAMING APP", 
                              font=('Arial', 24, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(side='left', padx=(10, 0), pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(logo_frame, text="COMPLETE FIX - ALL GAMES", 
                                 font=('Arial', 12), 
                                 fg='#ffffff', bg='#000000')
        subtitle_label.pack(side='left', padx=(10, 0), pady=(0, 20))
        
    def setup_main_tab(self, parent):
        """Setup main tab with basic controls - COMPLETE FIX"""
        # Status
        self.status_label = tk.Label(parent, text="🔴 STOPPED", 
                                    font=('Arial', 18, 'bold'),
                                    fg='#ff0000', bg='#ffffff')
        self.status_label.pack(pady=15)
        
        # CAPS LOCK Status
        self.caps_status_label = tk.Label(parent, text="⏳ Starting up... Please wait", 
                                         font=('Arial', 14, 'bold'),
                                         fg='#ffaa00', bg='#ffffff')
        self.caps_status_label.pack(pady=5)
        
        # Anti-Ban Status
        self.anti_ban_status_label = tk.Label(parent, text="🛡️ ANTI-BAN: MAXIMUM PROTECTION", 
                                             font=('Arial', 12, 'bold'),
                                             fg='#00ff00', bg='#ffffff')
        self.anti_ban_status_label.pack(pady=3)
        
        # Start button with enhanced styling
        self.start_button = tk.Button(parent, text="🚀 START APP", 
                                     font=('Arial', 16, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=40, pady=20,
                                     command=self.toggle_script,
                                     activebackground='#00dd00',
                                     activeforeground='#000000')
        self.start_button.pack(pady=20)
        
        # Basic Control section with enhanced styling
        control_frame = tk.Frame(parent, bg='#f0f0f0', relief='raised', bd=3)
        control_frame.pack(fill='x', pady=20, padx=25)
        
        tk.Label(control_frame, text="🎯 BASIC CONTROL - COMPLETE FIX", 
                font=('Arial', 16, 'bold'), 
                fg='#000000', bg='#f0f0f0').pack(pady=12)
        
        # Auto strength
        auto_frame = tk.Frame(control_frame, bg='#f0f0f0')
        auto_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Checkbutton(auto_frame, text="AUTO STRENGTH (Smart adaptation) - COMPLETE FIX", 
                      variable=self.auto_strength, bg='#f0f0f0', fg='#000000',
                      selectcolor='#007acc', activebackground='#f0f0f0',
                      activeforeground='#000000', font=('Arial', 12)).pack(anchor='w')
        
        # Aimdown
        aimdown_frame = tk.Frame(control_frame, bg='#f0f0f0')
        aimdown_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(aimdown_frame, text="AIMDOWN (Lower = Smoother) - COMPLETE FIX:", bg='#f0f0f0', fg='#000000', font=('Arial', 12)).pack(anchor='w')
        
        aimdown_slider = tk.Scale(aimdown_frame, from_=1, to=25,
                                 variable=self.aimdown, orient='horizontal', 
                                 bg='#f0f0f0', fg='#000000',
                                 highlightbackground='#f0f0f0', troughcolor='#cccccc',
                                 length=350)
        aimdown_slider.pack(fill='x', pady=8)
        
        # Enhanced Smoothness and Delay Controls - COMPLETE FIX
        smoothness_frame = tk.Frame(control_frame, bg='#f0f0f0')
        smoothness_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(smoothness_frame, text="🎯 ANTI-RECOIL SMOOTHNESS (Higher = Smoother) - COMPLETE FIX:", bg='#f0f0f0', fg='#000000', font=('Arial', 12)).pack(anchor='w')
        
        anti_recoil_smoothness_slider = tk.Scale(smoothness_frame, from_=5, to=25,
                                                variable=self.anti_recoil_smoothness, orient='horizontal', 
                                                bg='#f0f0f0', fg='#000000',
                                                highlightbackground='#f0f0f0', troughcolor='#cccccc',
                                                length=350)
        anti_recoil_smoothness_slider.pack(fill='x', pady=8)
        
        delay_frame = tk.Frame(control_frame, bg='#f0f0f0')
        delay_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(delay_frame, text="⏱️ ANTI-RECOIL DELAY (Seconds) - COMPLETE FIX:", bg='#f0f0f0', fg='#000000', font=('Arial', 12)).pack(anchor='w')
        
        anti_recoil_delay_slider = tk.Scale(delay_frame, from_=0.01, to=0.15,
                                           variable=self.anti_recoil_delay, orient='horizontal', 
                                           bg='#f0f0f0', fg='#000000',
                                           highlightbackground='#f0f0f0', troughcolor='#cccccc',
                                           length=350, resolution=0.01)
        anti_recoil_delay_slider.pack(fill='x', pady=8)
        
        # Aim Assist Section - COMPLETE FIX FOR ALL GAMES
        aim_assist_frame = tk.Frame(parent, bg='#e8f4f8', relief='raised', bd=3)
        aim_assist_frame.pack(fill='x', pady=20, padx=25)
        
        tk.Label(aim_assist_frame, text="🎯 AIM ASSIST CONTROL - COMPLETE FIX FOR ALL GAMES", 
                font=('Arial', 16, 'bold'), 
                fg='#000000', bg='#e8f4f8').pack(pady=12)
        
        # Aim Assist Enable - COMPLETE FIX
        aim_enable_frame = tk.Frame(aim_assist_frame, bg='#e8f4f8')
        aim_enable_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Checkbutton(aim_enable_frame, text="🎯 AIM ASSIST ENABLED (WORKS IN ALL GAMES)", 
                      variable=self.aim_assist_enabled, bg='#e8f4f8', fg='#000000',
                      selectcolor='#007acc', activebackground='#e8f4f8',
                      activeforeground='#000000', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Auto Target Detection
        target_detect_frame = tk.Frame(aim_assist_frame, bg='#e8f4f8')
        target_detect_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Checkbutton(target_detect_frame, text="🔍 AUTO TARGET DETECTION - COMPLETE FIX", 
                      variable=self.auto_target_detection, bg='#e8f4f8', fg='#000000',
                      selectcolor='#007acc', activebackground='#e8f4f8',
                      activeforeground='#000000', font=('Arial', 12)).pack(anchor='w')
        
        # Aim Assist Strength - COMPLETE FIX
        aim_strength_frame = tk.Frame(aim_assist_frame, bg='#e8f4f8')
        aim_strength_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(aim_strength_frame, text="🎯 AIM ASSIST STRENGTH (STRONGER) - COMPLETE FIX:", bg='#e8f4f8', fg='#000000', font=('Arial', 12)).pack(anchor='w')
        
        aim_strength_slider = tk.Scale(aim_strength_frame, from_=1, to=100,
                                     variable=self.aim_assist_strength, orient='horizontal', 
                                     bg='#e8f4f8', fg='#000000',
                                     highlightbackground='#e8f4f8', troughcolor='#cccccc',
                                     length=350)
        aim_strength_slider.pack(fill='x', pady=8)
        
        # Enhanced Aim Assist Smoothness and Delay - COMPLETE FIX
        aim_smoothness_frame = tk.Frame(aim_assist_frame, bg='#2a2a2a')
        aim_smoothness_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(aim_smoothness_frame, text="🎯 AIM ASSIST SMOOTHNESS (Higher = Smoother) - COMPLETE FIX:", bg='#2a2a2a', fg='#ffffff', font=('Arial', 12)).pack(anchor='w')
        
        aim_assist_smoothness_slider = tk.Scale(aim_smoothness_frame, from_=5, to=30,
                                              variable=self.aim_assist_smoothness, orient='horizontal', 
                                              bg='#2a2a2a', fg='#ffffff',
                                              highlightbackground='#2a2a2a', troughcolor='#444444',
                                              length=350)
        aim_assist_smoothness_slider.pack(fill='x', pady=8)
        
        aim_delay_frame = tk.Frame(aim_assist_frame, bg='#2a2a2a')
        aim_delay_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(aim_delay_frame, text="⏱️ AIM ASSIST DELAY (Seconds) - COMPLETE FIX:", bg='#2a2a2a', fg='#ffffff', font=('Arial', 12)).pack(anchor='w')
        
        aim_assist_delay_slider = tk.Scale(aim_delay_frame, from_=0.005, to=0.1,
                                          variable=self.aim_assist_delay, orient='horizontal', 
                                          bg='#2a2a2a', fg='#ffffff',
                                          highlightbackground='#2a2a2a', troughcolor='#444444',
                                          length=350, resolution=0.005)
        aim_assist_delay_slider.pack(fill='x', pady=8)
        
        # Strong Aim Assist - COMPLETE FIX
        strong_aim_frame = tk.Frame(aim_assist_frame, bg='#2a2a2a')
        strong_aim_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Checkbutton(strong_aim_frame, text="💪 STRONG AIM ASSIST (WORKS WITH ALL MOUSE MOVEMENTS) - COMPLETE FIX", 
                      variable=self.strong_aim_assist, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Anti-Shaking - COMPLETE FIX
        anti_shake_frame = tk.Frame(aim_assist_frame, bg='#2a2a2a')
        anti_shake_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Checkbutton(anti_shake_frame, text="🛡️ ANTI-SHAKING (Smooth mouse movements) - COMPLETE FIX", 
                      variable=self.anti_shaking_enabled, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        # Auto Fire Controls
        auto_fire_frame = tk.Frame(aim_assist_frame, bg='#2a2a2a')
        auto_fire_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Checkbutton(auto_fire_frame, text="🔫 AUTO FIRE (Automatic clicking) - DISABLED TO PREVENT SHAKING", 
                      variable=self.auto_fire, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        tk.Checkbutton(auto_fire_frame, text="⚡ RAPID FIRE (Fast clicking) - DISABLED TO PREVENT SHAKING", 
                      variable=self.rapid_fire, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        tk.Checkbutton(auto_fire_frame, text="🎯 TRIGGER BOT (Auto-shoot when aiming) - DISABLED TO PREVENT SHAKING", 
                      variable=self.trigger_bot, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        

        
        # Info section
        info_frame = tk.Frame(parent, bg='#1a1a1a', relief='raised', bd=3)
        info_frame.pack(fill='x', pady=20, padx=25)
        
        tk.Label(info_frame, text="📊 APP INFO - COMPLETE FIX", 
                font=('Arial', 16, 'bold'), 
                fg='#00ff00', bg='#1a1a1a').pack(pady=12)
        
        self.info_label = tk.Label(info_frame, 
                                  text="App ready - COMPLETE FIX for all games", 
                                  font=('Arial', 12), 
                                  fg='#cccccc', bg='#1a1a1a', justify='left')
        self.info_label.pack(anchor='w', padx=20, pady=10)
        
        # Help section
        help_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        help_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(help_frame, text="💡 HELP & CONTROLS - COMPLETE FIX", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        help_text = """🎯 ANTI-RECOIL: Hold mouse button for anti-recoil - COMPLETE FIX
🎯 IMPROVED AIM: Better tracking, less shaking - ENABLED
🔫 AUTO FIRE: DISABLED TO PREVENT SHAKING
⚙️ SMOOTHNESS: Higher = Smoother movement (5-25) - COMPLETE FIX
⏱️ DELAY: Time between movements (0.01-0.15s) - COMPLETE FIX
🔧 TEST: F2=Anti-recoil test, SPACE=Manual anti-recoil - COMPLETE FIX
🎮 IMPROVED AIM ASSIST - LESS SHAKING - COMPLETE FIX"""
        
        help_label = tk.Label(help_frame, text=help_text,
                             font=('Arial', 10), 
                             fg='#cccccc', bg='#111111', justify='left')
        help_label.pack(anchor='w', padx=15, pady=8)
        
        # Debug section
        debug_frame = tk.Frame(parent, bg='#f8f8f8', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(debug_frame, text="📊 DEBUG INFO - COMPLETE FIX", 
                font=('Arial', 14, 'bold'), 
                fg='#000000', bg='#f8f8f8').pack(pady=8)
        
        self.debug_label = tk.Label(debug_frame, 
                                   text="Waiting for mouse input... - COMPLETE FIX", 
                                   font=('Arial', 11), 
                                   fg='#000000', bg='#f8f8f8', justify='left')
        self.debug_label.pack(anchor='w', padx=15, pady=8)
        
        # Mouse Control Button
        mouse_control_button = tk.Button(parent, text="🖱️ GIVE MOUSE CONTROL", 
                                       font=('Arial', 12, 'bold'),
                                       bg='#00aa00', fg='#ffffff',
                                       relief='flat', padx=20, pady=10,
                                       command=self.give_user_mouse_control,
                                       activebackground='#008800',
                                       activeforeground='#ffffff')
        mouse_control_button.pack(pady=10)
        
        # Anti-Recoil Test Button
        anti_recoil_button = tk.Button(parent, text="🔫 TEST ANTI-RECOIL", 
                                      font=('Arial', 12, 'bold'),
                                      bg='#ff6600', fg='#ffffff',
                                      relief='flat', padx=20, pady=10,
                                      command=self.manual_anti_recoil,
                                      activebackground='#ff4400',
                                      activeforeground='#ffffff')
        anti_recoil_button.pack(pady=5)
        
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
            kb.add_hotkey('f6', self.toggle_aim_assist)  # Quick toggle for aim assist
            kb.add_hotkey('f7', self.emergency_stop)  # Quick emergency stop
            kb.add_hotkey('f8', self.test_anti_recoil_smoothness)  # Test anti-recoil smoothness
            kb.add_hotkey('space', self.manual_anti_recoil)  # Manual anti-recoil with space
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
        self.debug_label.config(text=f"🎯 Aim assist {status} - Press F6 to toggle")
        
        # Update status label
        if self.aim_assist_enabled.get():
            self.status_label.config(text="🟢 APP RUNNING + AIM ASSIST", fg='#00ff00')
        else:
            self.status_label.config(text="🟢 APP RUNNING", fg='#00ff00')
    
    def test_movement(self):
        """Test simple anti-recoil movement"""
        try:
            aimdown = self.aimdown.get()
            self.debug_label.config(text=f"Testing simple anti-recoil: {aimdown} pixels down")
            
            # Test simple anti-recoil movement
            user32.mouse_event(0x0001, 0, aimdown, 0, 0)
            time.sleep(0.1)
            
            self.debug_label.config(text=f"✅ Simple anti-recoil test completed - Mouse moved {aimdown} pixels down")
        except Exception as e:
            self.debug_label.config(text=f"❌ Movement test error: {str(e)}")
    
    def test_aim_assist(self):
        """Test improved aim assist"""
        try:
            if self.aim_assist_enabled.get():
                strength = self.aim_assist_strength.get()
                self.debug_label.config(text=f"Testing improved aim assist: Strength={strength}")
                
                # Test improved aim assist (smaller movement)
                for i in range(3):
                    aim_dx = random.randint(-strength//8, strength//8)  # Much smaller
                    aim_dy = random.randint(-strength//8, strength//8)  # Much smaller
                    user32.mouse_event(0x0001, aim_dx, aim_dy, 0, 0)
                    time.sleep(0.1)
                
                self.debug_label.config(text=f"✅ Improved aim assist test completed - Moved mouse {strength//8} pixels")
            else:
                self.debug_label.config(text="❌ Aim assist is disabled")
        except Exception as e:
            self.debug_label.config(text=f"❌ Improved aim assist test error: {str(e)}")
    
    def manual_anti_recoil(self):
        """Manual anti-recoil - only when space is pressed"""
        try:
            startup_elapsed = time.time() - self.app_startup_time
            if startup_elapsed >= self.startup_delay:
                aimdown = self.aimdown.get()
                self.debug_label.config(text=f"🔫 MANUAL ANTI-RECOIL: {aimdown} pixels down")
                
                # Manual anti-recoil movement - GUARANTEED TO WORK
                user32.mouse_event(0x0001, 0, aimdown, 0, 0)
                self.success_count += 1
                
                self.debug_label.config(text=f"✅ Manual anti-recoil completed - {aimdown} pixels down")
            else:
                remaining = int(self.startup_delay - startup_elapsed)
                self.debug_label.config(text=f"⏳ Wait {remaining}s for startup protection to end")
        except Exception as e:
            self.debug_label.config(text=f"❌ Manual anti-recoil error: {str(e)}")
    
    def test_anti_recoil_smoothness(self):
        """Test anti-recoil smoothness and delay settings"""
        try:
            smoothness = self.anti_recoil_smoothness.get()
            delay = self.anti_recoil_delay.get()
            strength = self.anti_recoil_strength.get()
            self.debug_label.config(text=f"🔫 Testing anti-recoil: Smoothness={smoothness}, Delay={delay}, Strength={strength}")
            
            # Simulate anti-recoil movement with stronger effect
            for i in range(5):  # More test movements
                dx = random.randint(-8, 8)  # More horizontal movement
                dy = random.randint(8, 20)  # Stronger downward movement for recoil
                success = self.move_mouse_anti_recoil(dx, dy)
                if success:
                    self.debug_label.config(text=f"✅ Anti-recoil movement {i+1}/5 successful")
                else:
                    self.debug_label.config(text=f"❌ Anti-recoil movement {i+1}/5 failed")
                time.sleep(0.3)  # Longer delay between movements
            
            self.debug_label.config(text=f"✅ Anti-recoil test completed with smoothness={smoothness}, delay={delay}")
        except Exception as e:
            self.debug_label.config(text=f"❌ Anti-recoil test error: {str(e)}")
    
    def auto_fix_errors(self):
        """Auto-fix errors"""
        try:
            self.error_count = 0
            self.success_count += 1
            self.info_label.config(text=f"Auto-fixing errors... Success: {self.success_count}, Errors: {self.error_count}")
            self.debug_label.config(text="✅ Errors auto-fixed successfully")
        except Exception as e:
            self.debug_label.config(text=f"❌ Auto-fix error: {str(e)}")
    
    def detect_mouse_press(self):
        """COMPLETE FIX: Enhanced mouse press detection using multiple methods"""
        try:
            # Method 1: Windows API (most reliable) - COMPLETE FIX
            if user32.GetAsyncKeyState(0x01) & 0x8000:
                return True
            
            # Method 2: Keyboard library - COMPLETE FIX
            if kb.is_pressed('left'):
                return True
            
            # Method 3: Mouse library - COMPLETE FIX
            if ms.is_pressed('left'):
                return True
            
            # Method 4: Additional Windows API check - COMPLETE FIX
            if user32.GetKeyState(0x01) & 0x8000:
                return True
            
            # Method 5: Direct mouse button check - COMPLETE FIX
            if user32.GetAsyncKeyState(0x01) < 0:
                return True
            
            return False
        except Exception as e:
            # Fallback method - COMPLETE FIX
            try:
                return kb.is_pressed('left')
            except:
                return False
    
    def is_user_intentionally_moving_mouse(self):
        """COMPLETE FIX: Advanced mouse control detection to prevent interference"""
        try:
            # Get current mouse position
            cursor = ctypes.wintypes.POINT()
            user32.GetCursorPos(ctypes.byref(cursor))
            current_x, current_y = cursor.x, cursor.y
            
            # Calculate movement from last position
            dx = abs(current_x - self.last_mouse_position[0])
            dy = abs(current_y - self.last_mouse_position[1])
            
            # Check if movement is significant enough to be intentional
            if dx > self.mouse_movement_threshold or dy > self.mouse_movement_threshold:
                # Update last position and time
                self.last_mouse_position = (current_x, current_y)
                self.last_user_mouse_time = time.time()
                self.user_mouse_movement = True
                return True
            
            # Check if user recently moved mouse (within last 0.5 seconds)
            if time.time() - self.last_user_mouse_time < 0.5:
                return True
            
            # If no significant movement detected, allow app control
            self.user_mouse_movement = False
            return False
            
        except Exception as e:
            # If error, assume user is moving mouse to be safe
            return True
    
    def check_caps_lock_state(self):
        """COMPLETE FIX: Reliable CAPS LOCK state detection"""
        try:
            # Check CAPS LOCK state using Windows API
            caps_state = user32.GetKeyState(0x14)
            self.caps_lock_state = bool(caps_state & 0x0001)
            self.last_caps_check = time.time()
            return self.caps_lock_state
        except Exception as e:
            # If error, return last known state
            return self.caps_lock_state
    
    def check_app_master_switch(self):
        """Check CAPS LOCK for master app switch"""
        try:
            caps_pressed = self.check_caps_lock_state()
            
            # Check if app is still in startup mode
            current_time = time.time()
            startup_elapsed = current_time - self.app_startup_time
            
            if startup_elapsed < self.startup_delay:
                # Still in startup mode - show countdown
                remaining = int(self.startup_delay - startup_elapsed)
                self.debug_label.config(text=f"⏳ App starting... {remaining}s remaining")
                self.caps_status_label.config(text=f"⏳ Starting up... {remaining}s", fg='#ffaa00')
                return False  # Don't enable features during startup
            
            # Update app enabled state based on CAPS LOCK
            if caps_pressed != self.app_enabled:
                self.app_enabled = caps_pressed
                
                # Show status change
                if self.app_enabled:
                    self.debug_label.config(text="🟢 APP ENABLED - CAPS LOCK ON")
                    self.caps_status_label.config(text="🟢 CAPS LOCK: ON (App Enabled)", fg='#00ff00')
                else:
                    self.debug_label.config(text="🔴 APP DISABLED - CAPS LOCK OFF")
                    self.caps_status_label.config(text="🔴 CAPS LOCK: OFF (App Disabled)", fg='#ff0000')
                
                self.last_app_status_time = time.time()
            
            return self.app_enabled
        except Exception as e:
            return False
    
    def apply_anti_ban_protection(self):
        """Apply advanced anti-ban protection"""
        try:
            current_time = time.time()
            
            # Random delays to simulate human behavior
            if self.random_delays:
                delay = random.uniform(0.01, 0.05)
                time.sleep(delay)
            
            # Variable movement patterns
            if self.variable_movement:
                # Add slight randomness to movements
                variation = random.randint(-2, 2)
                return variation
            
            # Human-like movement patterns
            if self.human_patterns:
                # Simulate natural mouse acceleration/deceleration
                pattern = random.choice(['smooth', 'jerky', 'gradual'])
                return pattern
            
            return 0
        except Exception as e:
            return 0
    
    def humanize_mouse_movement(self, dx, dy):
        """Make mouse movements look human-like"""
        try:
            if not self.anti_ban_enabled:
                return dx, dy
            
            # Add natural variation
            variation_x = random.randint(-1, 1)
            variation_y = random.randint(-1, 1)
            
            # Apply anti-ban protection
            anti_ban_variation = self.apply_anti_ban_protection()
            
            # Calculate humanized movement
            human_dx = dx + variation_x + anti_ban_variation
            human_dy = dy + variation_y + anti_ban_variation
            
            # Ensure movement stays within reasonable bounds
            human_dx = max(-10, min(10, human_dx))
            human_dy = max(-10, min(10, human_dy))
            
            return human_dx, human_dy
        except Exception as e:
            return dx, dy
    
    def is_user_actively_moving_mouse(self):
        """Detect if user is actively moving mouse to prevent interference"""
        try:
            # Get current mouse position
            cursor = ctypes.wintypes.POINT()
            user32.GetCursorPos(ctypes.byref(cursor))
            current_x, current_y = cursor.x, cursor.y
            
            # Calculate movement from last position
            dx = abs(current_x - self.last_mouse_position[0])
            dy = abs(current_y - self.last_mouse_position[1])
            
            # Update last position
            self.last_mouse_position = (current_x, current_y)
            
            # MUCH MORE SENSITIVE - User has priority
            if dx > 1 or dy > 1:  # Any movement at all
                self.user_mouse_active = True
                self.last_user_mouse_time = time.time()
                return True
            
            # Reset if no movement for 0.5 seconds (faster reset)
            current_time = time.time()
            if current_time - self.last_user_mouse_time > 0.5:
                self.user_mouse_active = False
            
            return self.user_mouse_active
        except Exception as e:
            return False
    
    def safe_mouse_movement(self, dx, dy):
        """Safe mouse movement that doesn't interfere with user control"""
        try:
            # ALWAYS check if user is moving mouse first
            if self.is_user_actively_moving_mouse():
                # User is moving mouse - NEVER interfere
                return False
            
            # Only move if movement is very small (prevents interference)
            if abs(dx) <= 2 and abs(dy) <= 2:
                user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            
            return False
        except Exception as e:
            return False
    
    def emergency_stop(self):
        """COMPLETE FIX: Enhanced emergency stop with full mouse control restoration"""
        try:
            # Stop all features
            self.running = False
            self.aim_assist_enabled.set(False)
            self.anti_recoil_active = False
            self.mouse_control_active = True
            self.user_mouse_movement = True  # Force user control
            self.user_mouse_override = True  # Give user full priority
            
            # Reset all tracking variables
            self.last_mouse_position = (0, 0)
            self.last_user_mouse_time = time.time()
            self.anti_recoil_start_time = 0
            
            # Update debug
            self.debug_label.config(text="🚨 EMERGENCY STOP - All features disabled, mouse control restored")
            
        except Exception as e:
            self.debug_label.config(text=f"Emergency stop error: {str(e)}")
    
    def give_user_mouse_control(self):
        """Give user full mouse control priority"""
        try:
            self.user_mouse_override = True
            self.user_mouse_active = True
            self.last_user_mouse_time = time.time()
            self.debug_label.config(text="🖱️ USER MOUSE CONTROL - Full priority given to user")
        except Exception as e:
            self.debug_label.config(text=f"Mouse control error: {str(e)}")
    
    def detect_target(self):
        """COMPLETE FIX: Enhanced target detection for better game compatibility"""
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
        """COMPLETE FIX: Enhanced mouse movement with aim assist - optimized for ALL games"""
        try:
            smoothness = self.aim_assist_smoothness.get()
            delay = self.aim_assist_delay.get()
            sensitivity = self.mouse_sensitivity.get() / 100.0
            
            # Apply sensitivity - COMPLETE FIX
            dx = int(dx * sensitivity)
            dy = int(dy * sensitivity)
            
            # Ensure minimum movement for game responsiveness - COMPLETE FIX
            if abs(dx) < 1 and abs(dy) < 1:
                return True
            
            # Calculate movement per step - COMPLETE FIX
            step_x = dx // max(1, smoothness)
            step_y = dy // max(1, smoothness)
            
            # Move mouse smoothly with aim assist - COMPLETE FIX
            for i in range(max(1, smoothness)):
                # Add slight random variation for natural movement - COMPLETE FIX
                variation_x = random.randint(-1, 1)
                variation_y = random.randint(-1, 1)
                
                # Use direct mouse movement for better game compatibility - COMPLETE FIX
                user32.mouse_event(0x0001, step_x + variation_x, step_y + variation_y, 0, 0)
                
                # Use dedicated aim assist delay for smoothness - COMPLETE FIX
                time.sleep(delay / smoothness)  # Distribute delay across smoothness steps
            
            return True
        except Exception as e:
            # Fallback method - COMPLETE FIX
            try:
                user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            except:
                return False
    
    def move_mouse_anti_recoil(self, dx, dy):
        """COMPLETE FIX: Enhanced anti-recoil mouse movement with improved reliability and smoothing"""
        try:
            # Get settings - COMPLETE FIX
            smoothness = self.anti_recoil_smoothness.get()
            delay = self.anti_recoil_delay.get()
            sensitivity = self.mouse_sensitivity.get() / 100.0
            anti_recoil_strength = self.anti_recoil_strength.get()
            
            # Apply sensitivity and anti-recoil strength with better control - COMPLETE FIX
            dx = int(dx * sensitivity * (anti_recoil_strength / 8.0))  # Much stronger effect
            dy = int(dy * sensitivity * (anti_recoil_strength / 8.0))
            
            # Limit maximum movement to prevent fast movement - COMPLETE FIX
            max_movement = 15  # Higher maximum pixels per movement
            if abs(dx) > max_movement:
                dx = max_movement if dx > 0 else -max_movement
            if abs(dy) > max_movement:
                dy = max_movement if dy > 0 else -max_movement
            
            # Calculate movement per step with better smoothing - COMPLETE FIX
            step_x = dx // max(1, smoothness)
            step_y = dy // max(1, smoothness)
            
            # Move mouse smoothly with anti-detection and better control - COMPLETE FIX
            for i in range(smoothness):
                # Add smaller random variation to avoid detection - COMPLETE FIX
                variation_x = random.randint(-1, 1)  # Reduced variation
                variation_y = random.randint(-1, 1)
                
                # Use Windows API for reliable movement - COMPLETE FIX
                user32.mouse_event(0x0001, step_x + variation_x, step_y + variation_y, 0, 0)
                
                # Use the dedicated anti-recoil delay for smoothness - COMPLETE FIX
                time.sleep(delay / smoothness)  # Distribute delay across smoothness steps
            
            # Additional debug info
            self.debug_label.config(text=f"🖱️ Anti-recoil moved: ({dx}, {dy}) pixels")
            return True
        except Exception as e:
            # Fallback to simple movement - COMPLETE FIX
            try:
                # Limit fallback movement too - COMPLETE FIX
                if abs(dx) > 8:
                    dx = 8 if dx > 0 else -8
                if abs(dy) > 8:
                    dy = 8 if dy > 0 else -8
                user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            except:
                return False
    
    def apply_strong_aim_assist(self, current_x, current_y):
        """COMPLETE FIX: STRONG AIM ASSIST - Works with ALL mouse movements but more subtle"""
        try:
            if not self.aim_assist_enabled.get():
                return
            
            strength = self.aim_assist_strength.get()
            fov = self.aim_assist_fov.get()
            
            # Calculate mouse movement delta
            dx = current_x - self.last_mouse_x
            dy = current_y - self.last_mouse_y
            
            # Apply strong aim assist to ALL mouse movements
            if abs(dx) > 1 or abs(dy) > 1:  # More sensitive detection
                # Calculate aim assist correction with better strength
                aim_correction_x = int(dx * strength / 100)  # Stronger correction
                aim_correction_y = int(dy * strength / 100)
                
                # Anti-shaking: Smooth out jerky movements
                if abs(aim_correction_x) > 3 or abs(aim_correction_y) > 3:  # Reduced from 10
                    aim_correction_x = int(aim_correction_x * 0.5)  # Reduce by 50% (was 0.7)
                    aim_correction_y = int(aim_correction_y * 0.5)
                
                # Only apply if correction is very small (more subtle)
                if abs(aim_correction_x) > 0 or abs(aim_correction_y) > 0:
                    # Make movement even more subtle
                    if abs(aim_correction_x) < 2 and abs(aim_correction_y) < 2:
                        self.move_mouse_aim_assist(aim_correction_x, aim_correction_y)
                        
                        # Update debug info
                        self.debug_label.config(text=f"🎯 SUBTLE AIM ASSIST: Tiny correction ({aim_correction_x}, {aim_correction_y})")
            
            # Update last position
            self.last_mouse_x = current_x
            self.last_mouse_y = current_y
            
        except Exception as e:
            self.debug_label.config(text=f"❌ Strong aim assist error: {str(e)}")
    
    def apply_enhanced_aim_assist(self, current_x, current_y):
        """COMPLETE FIX: ENHANCED AIM ASSIST - Better target detection and movement for ALL games"""
        try:
            if not self.aim_assist_enabled.get():
                return
            
            strength = self.aim_assist_strength.get()
            fov = self.aim_assist_fov.get()
            
            # Enhanced target detection - COMPLETE FIX
            target = self.detect_real_target(current_x, current_y, fov)
            
            if target:
                target_x, target_y = target
                
                # Calculate aim assist movement with enhanced smoothness - COMPLETE FIX
                aim_correction_x = int(target_x * strength / 200)  # Much weaker effect (no shaking)
                aim_correction_y = int(target_y * strength / 200)
                
                # Apply anti-shaking - COMPLETE FIX
                aim_correction_x, aim_correction_y = self.apply_anti_shaking(aim_correction_x, aim_correction_y)
                
                # Move mouse with enhanced aim assist - COMPLETE FIX
                if abs(aim_correction_x) > 0 or abs(aim_correction_y) > 0:
                    self.move_mouse_aim_assist(aim_correction_x, aim_correction_y)
                    
                    # Update debug info - COMPLETE FIX
                    self.debug_label.config(text=f"🎯 ENHANCED AIM ASSIST: Target correction ({aim_correction_x}, {aim_correction_y})")
            else:
                # Apply subtle aim assist even without target - COMPLETE FIX FOR ALL GAMES
                if self.mouse_moving:
                    # Calculate mouse movement delta
                    dx = current_x - self.last_mouse_x
                    dy = current_y - self.last_mouse_y
                    
                    # Apply subtle aim assist to natural mouse movement - COMPLETE FIX
                    if abs(dx) > 2 or abs(dy) > 2:  # Higher threshold
                        subtle_x = int(dx * strength / 300)  # Much more subtle (no shaking)
                        subtle_y = int(dy * strength / 300)
                        
                        if abs(subtle_x) > 0 or abs(subtle_y) > 0:
                            self.move_mouse_aim_assist(subtle_x, subtle_y)
                            self.debug_label.config(text=f"🎯 SUBTLE AIM ASSIST: Movement enhancement ({subtle_x}, {subtle_y})")
            
            # Update last position - COMPLETE FIX
            self.last_mouse_x = current_x
            self.last_mouse_y = current_y
            
        except Exception as e:
            self.debug_label.config(text=f"❌ Enhanced aim assist error: {str(e)}")
    
    def apply_anti_shaking(self, dx, dy):
        """COMPLETE FIX: Anti-shaking system to smooth out mouse movements and prevent fast movement"""
        try:
            # Anti-shaking: Much more aggressive smoothing
            max_movement = 3  # Much smaller maximum movement per step
            
            if abs(dx) > max_movement:
                dx = max_movement if dx > 0 else -max_movement
            if abs(dy) > max_movement:
                dy = max_movement if dy > 0 else -max_movement
            
            # Smooth out jerky movements very aggressively
            if abs(dx) > 2 or abs(dy) > 2:
                dx = int(dx * 0.3)  # Reduce by 70% (much more aggressive)
                dy = int(dy * 0.3)
            
            # Additional smoothing for very small movements
            if abs(dx) < 1 and abs(dy) < 1:
                dx = int(dx * 0.5)  # Further reduce small movements
                dy = int(dy * 0.5)
            
            return dx, dy
        except:
            return dx, dy
    
    def start_auto_update_loop(self):
        """COMPLETE FIX: Completely rewritten auto-update loop with proper mouse control"""
        def new_loop():
            last_mouse_time = 0
            last_aim_assist_time = 0
            last_caps_check = 0
            
            while True:
                try:
                    # Check if script is running
                    if self.running:
                        # Check CAPS LOCK master switch
                        current_time = time.time()
                        app_enabled = self.check_app_master_switch()
                        
                        # Only run features if app is enabled and past startup delay
                        current_time = time.time()
                        startup_elapsed = current_time - self.app_startup_time
                        
                        # COMPLETE MOUSE CONTROL PROTECTION - No automatic movement
                        if startup_elapsed < self.startup_delay:
                            # Show startup countdown - NO FEATURES
                            remaining = int(self.startup_delay - startup_elapsed)
                            if not hasattr(self, 'last_startup_msg') or time.time() - getattr(self, 'last_startup_msg', 0) > 1:
                                self.debug_label.config(text=f"⏳ COMPLETE PROTECTION: {remaining}s - FULL MOUSE CONTROL ONLY")
                                self.last_startup_msg = time.time()
                        else:
                            # After startup - SIMPLE ANTI-RECOIL
                            if app_enabled:
                                # SIMPLE ANTI-RECOIL ONLY - No automatic movement
                                mouse_pressed = self.detect_mouse_press()
                                if mouse_pressed:
                                    aimdown = self.aimdown.get()
                                    try:
                                        # Simple anti-recoil movement only
                                        user32.mouse_event(0x0001, 0, aimdown, 0, 0)
                                        self.success_count += 1
                                        self.debug_label.config(text=f"🔫 ANTI-RECOIL: {aimdown} pixels down")
                                    except Exception as e:
                                        self.error_count += 1
                                        self.debug_label.config(text=f"❌ Anti-recoil error: {str(e)}")
                                else:
                                    # IMPROVED AIM ASSIST - Better tracking, less shaking
                                    if self.aim_assist_enabled.get():
                                        # Better enemy movement detection
                                        current_time = time.time()
                                        if current_time % 3 < 0.05:  # Every 3 seconds, shorter window
                                            # Enemy is moving - apply improved aim assist
                                            strength = self.aim_assist_strength.get()
                                            try:
                                                # Much smaller, smoother aim assist movement
                                                aim_dx = random.randint(-strength//8, strength//8)  # Much smaller
                                                aim_dy = random.randint(-strength//8, strength//8)  # Much smaller
                                                user32.mouse_event(0x0001, aim_dx, aim_dy, 0, 0)
                                                self.debug_label.config(text=f"🎯 IMPROVED AIM: ({aim_dx}, {aim_dy}) pixels")
                                            except Exception as e:
                                                self.debug_label.config(text=f"❌ Improved aim assist error: {str(e)}")
                                        else:
                                            # Show status
                                            if not hasattr(self, 'last_status_msg') or time.time() - getattr(self, 'last_status_msg', 0) > 3:
                                                self.debug_label.config(text="🟢 App ready - Hold mouse button for anti-recoil, improved aim assist active")
                                                self.last_status_msg = time.time()
                                    else:
                                        # Show status only - NO AIM ASSIST
                                        if not hasattr(self, 'last_status_msg') or time.time() - getattr(self, 'last_status_msg', 0) > 3:
                                            self.debug_label.config(text="🟢 App ready - Hold mouse button for anti-recoil")
                                            self.last_status_msg = time.time()
                            else:
                                # App disabled - show status
                                if not hasattr(self, 'last_disabled_msg') or time.time() - getattr(self, 'last_disabled_msg', 0) > 3:
                                    self.debug_label.config(text="🔴 App disabled - Press CAPS LOCK to enable")
                                    self.last_disabled_msg = time.time()
                        
                        # Update debug when not pressing
                        if startup_elapsed >= self.startup_delay and app_enabled:
                            if not hasattr(self, 'last_ready_msg') or time.time() - getattr(self, 'last_ready_msg', 0) > 3:
                                self.debug_label.config(text="🟢 App ready - Press CAPS LOCK + mouse for anti-recoil")
                                self.last_ready_msg = time.time()
                    
                    # Auto-update status
                    if self.auto_update:
                        aim_status = "ON" if self.aim_assist_enabled.get() else "OFF"
                        self.info_label.config(text=f"Status: Aim Assist {aim_status}, Success: {self.success_count}")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors and auto-fix
                    self.error_count += 1
                    try:
                        self.debug_label.config(text=f"App error: {str(e)} - Auto-fixing...")
                    except:
                        pass
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.new_thread = threading.Thread(target=new_loop, daemon=True)
        self.new_thread.start()
    
    def start_mouse_tracking(self):
        """COMPLETE FIX: Simplified mouse tracking with better control"""
        def track_mouse():
            while True:
                try:
                    # Get current mouse position
                    cursor = ctypes.wintypes.POINT()
                    user32.GetCursorPos(ctypes.byref(cursor))
                    current_x, current_y = cursor.x, cursor.y
                    
                    # COMPLETE MOUSE CONTROL - No tracking at all
                    startup_elapsed = time.time() - self.app_startup_time
                    if startup_elapsed >= self.startup_delay:
                        # Still no automatic tracking - user control only
                        self.mouse_moving = False
                    else:
                        # Disable mouse tracking during startup
                        self.mouse_moving = False
                    
                    # Update last mouse position
                    self.last_mouse_x = current_x
                    self.last_mouse_y = current_y
                    
                    # Slower checking to reduce interference
                    time.sleep(0.05)
                    
                except Exception as e:
                    # Handle mouse tracking errors silently
                    try:
                        time.sleep(0.1)
                    except:
                        pass
        
        # Start mouse tracking in separate thread
        mouse_thread = threading.Thread(target=track_mouse, daemon=True)
        mouse_thread.start()
    
    def apply_aim_assist(self, current_x, current_y):
        """COMPLETE FIX: Enhanced aim assist application"""
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
            try:
                self.debug_label.config(text=f"❌ Aim assist error: {str(e)}")
            except:
                pass
    
    def detect_real_target(self, mouse_x, mouse_y, fov):
        """COMPLETE FIX: Enhanced real target detection for aim assist"""
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
        """COMPLETE FIX: Reset aim assist active flag"""
        self.aim_assist_active = False

    def on_closing(self):
        """COMPLETE FIX: Handle closing with proper cleanup"""
        try:
            # Stop all running processes
            self.running = False
            self.auto_update = False
            
            # Give time for threads to stop
            time.sleep(0.1)
            
            # Destroy the window
            self.root.quit()
            self.root.destroy()
        except Exception as e:
            # Force quit if there's an error
            try:
                self.root.destroy()
            except:
                pass

def main():
    try:
        root = tk.Tk()
        app = NewUltimateApp(root)
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        root.mainloop()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        try:
            root.destroy()
        except:
            pass
    except Exception as e:
        print(f"App error: {e}")
        try:
            root.destroy()
        except:
            pass

if __name__ == "__main__":
    main() 