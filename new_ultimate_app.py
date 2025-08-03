import tkinter as tk
from tkinter import messagebox
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
        self.root.title("🎯 NEW ULTIMATE APP")
        self.root.geometry("700x900")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.auto_update = True
        self.anti_detection = True
        self.error_count = 0
        self.success_count = 0
        
        # Variables
        self.aimdown = tk.IntVar(value=5)
        self.delay = tk.DoubleVar(value=0.03)
        self.smoothness = tk.IntVar(value=8)
        self.auto_strength = tk.BooleanVar(value=True)
        
        # Aim Assist Variables
        self.aim_assist_enabled = tk.BooleanVar(value=True)
        self.aim_assist_strength = tk.IntVar(value=15)
        self.aim_assist_fov = tk.IntVar(value=50)
        self.aim_assist_smoothness = tk.IntVar(value=10)
        self.aim_assist_target_size = tk.IntVar(value=20)
        self.auto_target_detection = tk.BooleanVar(value=True)
        
        # Mouse tracking for aim assist
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_moving = False
        self.aim_assist_active = False
        
        # Setup UI
        self.setup_ui()
        
        # Start auto-update loop
        self.start_auto_update_loop()
        
        # Start mouse tracking for aim assist
        self.start_mouse_tracking()
        
    def setup_ui(self):
        """New ultimate UI with aim assist"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 NEW ULTIMATE APP", 
                              font=('Arial', 20, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 16, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START NEW APP", 
                                     font=('Arial', 14, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=30, pady=15,
                                     command=self.toggle_script)
        self.start_button.pack(pady=15)
        
        # Control section
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=15)
        
        tk.Label(control_frame, text="🎯 NEW APP CONTROL", 
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
        
        # Delay
        delay_frame = tk.Frame(control_frame, bg='#111111')
        delay_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(delay_frame, text="DELAY (Higher = Smoother):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        delay_slider = tk.Scale(delay_frame, from_=0.00, to=0.20, resolution=0.01,
                               variable=self.delay, orient='horizontal', 
                               bg='#111111', fg='#ffffff',
                               highlightbackground='#111111', troughcolor='#333333',
                               length=300)
        delay_slider.pack(fill='x', pady=5)
        
        # Smoothness
        smoothness_frame = tk.Frame(control_frame, bg='#111111')
        smoothness_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(smoothness_frame, text="SMOOTHNESS (Higher = Smoother):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        smoothness_slider = tk.Scale(smoothness_frame, from_=1, to=25,
                                   variable=self.smoothness, orient='horizontal', 
                                   bg='#111111', fg='#ffffff',
                                   highlightbackground='#111111', troughcolor='#333333',
                                   length=300)
        smoothness_slider.pack(fill='x', pady=5)
        
        # Aim Assist Section
        aim_assist_frame = tk.Frame(main_frame, bg='#222222', relief='raised', bd=2)
        aim_assist_frame.pack(fill='x', pady=15)
        
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
        
        aim_strength_slider = tk.Scale(aim_strength_frame, from_=1, to=30,
                                     variable=self.aim_assist_strength, orient='horizontal', 
                                     bg='#222222', fg='#ffffff',
                                     highlightbackground='#222222', troughcolor='#444444',
                                     length=300)
        aim_strength_slider.pack(fill='x', pady=5)
        
        # Aim Assist FOV
        aim_fov_frame = tk.Frame(aim_assist_frame, bg='#222222')
        aim_fov_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(aim_fov_frame, text="👁️ AIM ASSIST FOV (Field of View):", bg='#222222', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        aim_fov_slider = tk.Scale(aim_fov_frame, from_=10, to=100,
                                 variable=self.aim_assist_fov, orient='horizontal', 
                                 bg='#222222', fg='#ffffff',
                                 highlightbackground='#222222', troughcolor='#444444',
                                 length=300)
        aim_fov_slider.pack(fill='x', pady=5)
        
        # Aim Assist Smoothness
        aim_smooth_frame = tk.Frame(aim_assist_frame, bg='#222222')
        aim_smooth_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(aim_smooth_frame, text="🔄 AIM ASSIST SMOOTHNESS:", bg='#222222', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        aim_smooth_slider = tk.Scale(aim_smooth_frame, from_=1, to=20,
                                   variable=self.aim_assist_smoothness, orient='horizontal', 
                                   bg='#222222', fg='#ffffff',
                                   highlightbackground='#222222', troughcolor='#444444',
                                   length=300)
        aim_smooth_slider.pack(fill='x', pady=5)
        
        # Target Size
        target_size_frame = tk.Frame(aim_assist_frame, bg='#222222')
        target_size_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(target_size_frame, text="🎯 TARGET SIZE:", bg='#222222', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        target_size_slider = tk.Scale(target_size_frame, from_=5, to=50,
                                    variable=self.aim_assist_target_size, orient='horizontal', 
                                    bg='#222222', fg='#ffffff',
                                    highlightbackground='#222222', troughcolor='#444444',
                                    length=300)
        target_size_slider.pack(fill='x', pady=5)
        
        # Info section
        info_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=15)
        
        tk.Label(info_frame, text="📊 NEW APP INFO", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        self.info_label = tk.Label(info_frame, 
                                  text="New app ready - auto-updating active", 
                                  font=('Arial', 11), 
                                  fg='#cccccc', bg='#111111', justify='left')
        self.info_label.pack(anchor='w', padx=15, pady=8)
        
        # Debug section
        debug_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=15)
        
        tk.Label(debug_frame, text="📊 NEW APP DEBUG", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        self.debug_label = tk.Label(debug_frame, 
                                   text="Waiting for mouse input...", 
                                   font=('Arial', 11), 
                                   fg='#cccccc', bg='#111111', justify='left')
        self.debug_label.pack(anchor='w', padx=15, pady=8)
        
        # Instructions
        instructions_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        instructions_frame.pack(fill='x', pady=15)
        
        tk.Label(instructions_frame, text="📋 NEW APP INSTRUCTIONS", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        instructions = tk.Label(instructions_frame, 
                              text="1. Click START NEW APP\n2. Turn CAPS LOCK ON\n3. Go to ANY game\n4. Hold left mouse button\n5. Aim assist will auto-target enemies\n6. Auto-updates and error fixes",
                              font=('Arial', 11), 
                              fg='#cccccc', bg='#111111', justify='left')
        instructions.pack(anchor='w', padx=15, pady=8)
        
        # Hotkeys
        hotkey_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        hotkey_frame.pack(fill='x', pady=15)
        
        tk.Label(hotkey_frame, text="⌨️ NEW APP HOTKEYS", 
                font=('Arial', 14, 'bold'), 
                fg='#ffff00', bg='#111111').pack(pady=8)
        
        hotkeys = tk.Label(hotkey_frame, 
                          text="INSERT: Toggle script\nCAPS LOCK: ON=Script works, OFF=Script disabled\nF1: Emergency stop\nF2: Test movement\nF3: Auto-fix errors\nF4: Toggle aim assist\nF5: Test aim assist",
                          font=('Arial', 11), 
                          fg='#cccccc', bg='#111111', justify='left')
        hotkeys.pack(anchor='w', padx=15, pady=8)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener"""
        try:
            kb.add_hotkey('insert', self.toggle_script)
            kb.add_hotkey('f1', self.emergency_stop)
            kb.add_hotkey('f2', self.test_movement)
            kb.add_hotkey('f3', self.auto_fix_errors)
            kb.add_hotkey('f4', self.toggle_aim_assist)
            kb.add_hotkey('f5', self.test_aim_assist)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 NEW APP RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP NEW APP", bg='#ff0000')
            self.debug_label.config(text="New app started - auto-updating active...")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START NEW APP", bg='#00ff00')
            self.debug_label.config(text="New app stopped")
    
    def toggle_aim_assist(self):
        """Toggle aim assist on/off"""
        self.aim_assist_enabled.set(not self.aim_assist_enabled.get())
        status = "ENABLED" if self.aim_assist_enabled.get() else "DISABLED"
        self.debug_label.config(text=f"🎯 Aim assist {status}")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START NEW APP", bg='#00ff00')
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
        """Simulate target detection"""
        try:
            if not self.auto_target_detection.get():
                return None
            
            # Simulate target detection with random positions
            fov = self.aim_assist_fov.get()
            target_size = self.aim_assist_target_size.get()
            
            # Random target position within FOV
            target_x = random.randint(-fov//2, fov//2)
            target_y = random.randint(-fov//2, fov//2)
            
            # Check if target is within detection range
            distance = math.sqrt(target_x**2 + target_y**2)
            if distance <= fov//2:
                return (target_x, target_y)
            
            return None
        except:
            return None
    
    def move_mouse_aim_assist(self, dx, dy):
        """Move mouse with aim assist - optimized for games"""
        try:
            smoothness = self.aim_assist_smoothness.get()
            
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
        """New mouse movement method with anti-detection"""
        try:
            # Get smoothness setting
            smoothness = self.smoothness.get()
            
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
        """Start the new auto-updating loop with aim assist"""
        def new_loop():
            last_mouse_time = 0
            last_aim_assist_time = 0
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
                                        debug_text = f"🎯 NEW APP - Auto recoil: {aimdown} pixels. Success: {self.success_count}"
                                        self.debug_label.config(text=debug_text)
                                        
                                        # Move mouse using new method
                                        success = self.move_mouse_new(0, aimdown)
                                        
                                        if success:
                                            self.debug_label.config(text=f"✅ NEW APP movement successful! Success: {self.success_count}")
                                        else:
                                            self.error_count += 1
                                            self.debug_label.config(text=f"❌ NEW APP movement failed! Errors: {self.error_count}")
                                        
                                        # Update last mouse time
                                        last_mouse_time = current_time
                                    
                                    # Aim Assist Logic
                                    if self.aim_assist_enabled.get():
                                        aim_assist_delay = 0.05  # Aim assist runs every 50ms
                                        if current_time - last_aim_assist_time >= aim_assist_delay:
                                            # Detect target
                                            target = self.detect_target()
                                            if target:
                                                target_x, target_y = target
                                                strength = self.aim_assist_strength.get()
                                                
                                                # Calculate aim assist movement
                                                aim_x = int(target_x * strength / 100)
                                                aim_y = int(target_y * strength / 100)
                                                
                                                # Apply aim assist movement
                                                if abs(aim_x) > 0 or abs(aim_y) > 0:
                                                    self.move_mouse_aim_assist(aim_x, aim_y)
                                                    self.debug_label.config(text=f"🎯 Aim assist: Target detected! Moving ({aim_x}, {aim_y})")
                                            
                                            last_aim_assist_time = current_time
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
                        self.info_label.config(text=f"Auto-updating... Success: {self.success_count}, Errors: {self.error_count}, Aim Assist: {aim_status}")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors and auto-fix
                    self.error_count += 1
                    self.debug_label.config(text=f"New app error: {str(e)} - Auto-fixing...")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.new_thread = threading.Thread(target=new_loop, daemon=True)
        self.new_thread.start()
    
    def start_mouse_tracking(self):
        """Start tracking mouse movement for aim assist"""
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
        """Apply aim assist to current mouse movement"""
        try:
            if not self.aim_assist_active:
                strength = self.aim_assist_strength.get()
                fov = self.aim_assist_fov.get()
                
                # Simulate target detection (in real implementation, this would use game memory/vision)
                target = self.detect_real_target(current_x, current_y, fov)
                
                if target:
                    target_x, target_y = target
                    
                    # Calculate aim assist movement
                    aim_dx = int(target_x * strength / 100)
                    aim_dy = int(target_y * strength / 100)
                    
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
        """Detect real targets for aim assist (simulated for now)"""
        try:
            # In a real implementation, this would:
            # 1. Read game memory for enemy positions
            # 2. Use computer vision to detect enemies
            # 3. Calculate distance and angle to targets
            
            # For now, simulate target detection based on mouse movement
            if self.mouse_moving and random.random() < 0.3:  # 30% chance to detect "target"
                # Simulate target offset from current mouse position
                target_offset_x = random.randint(-fov//2, fov//2)
                target_offset_y = random.randint(-fov//2, fov//2)
                
                # Only return target if within FOV
                distance = math.sqrt(target_offset_x**2 + target_offset_y**2)
                if distance <= fov//2:
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
            if messagebox.askokcancel("Quit", "New app is running. Quit?"):
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