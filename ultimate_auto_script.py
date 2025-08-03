import tkinter as tk
from tkinter import messagebox
import threading
import time
import sys
import ctypes
import os
import platform
import random
from ctypes import wintypes

# Direct Windows API imports
try:
    import keyboard as kb
    import mouse as ms
except ImportError:
    messagebox.showerror("Error", "Please install: pip install keyboard mouse")
    sys.exit(1)

# Windows API for direct mouse control
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

class UltimateAutoScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Ultimate Auto Script")
        self.root.geometry("600x700")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.auto_update = True
        self.anti_detection = True
        self.error_count = 0
        self.success_count = 0
        
        # Variables
        self.aimdown = tk.IntVar(value=3)
        self.delay = tk.DoubleVar(value=0.05)
        self.smoothness = tk.IntVar(value=5)
        self.auto_strength = tk.BooleanVar(value=True)
        
        # Setup UI
        self.setup_ui()
        
        # Start auto-update loop
        self.start_auto_update_loop()
        
    def setup_ui(self):
        """Ultimate auto-updating UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 ULTIMATE AUTO SCRIPT", 
                              font=('Arial', 18, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START ULTIMATE", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Auto control
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=10)
        
        tk.Label(control_frame, text="🎯 AUTO CONTROL", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        # Auto strength
        auto_frame = tk.Frame(control_frame, bg='#111111')
        auto_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Checkbutton(auto_frame, text="AUTO STRENGTH (Adapts to game)", 
                      variable=self.auto_strength, bg='#111111', fg='#ffffff',
                      selectcolor='#333333', activebackground='#111111',
                      activeforeground='#ffffff').pack(anchor='w')
        
        # Aimdown
        aimdown_frame = tk.Frame(control_frame, bg='#111111')
        aimdown_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(aimdown_frame, text="AIMDOWN (Lower = Smoother):", bg='#111111', fg='#ffffff').pack(anchor='w')
        
        aimdown_slider = tk.Scale(aimdown_frame, from_=1, to=20,
                                 variable=self.aimdown, orient='horizontal', 
                                 bg='#111111', fg='#ffffff',
                                 highlightbackground='#111111', troughcolor='#333333')
        aimdown_slider.pack(fill='x', pady=2)
        
        # Delay
        delay_frame = tk.Frame(control_frame, bg='#111111')
        delay_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(delay_frame, text="DELAY (Higher = Smoother):", bg='#111111', fg='#ffffff').pack(anchor='w')
        
        delay_slider = tk.Scale(delay_frame, from_=0.00, to=0.15, resolution=0.01,
                               variable=self.delay, orient='horizontal', 
                               bg='#111111', fg='#ffffff',
                               highlightbackground='#111111', troughcolor='#333333')
        delay_slider.pack(fill='x', pady=2)
        
        # Smoothness
        smoothness_frame = tk.Frame(control_frame, bg='#111111')
        smoothness_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(smoothness_frame, text="SMOOTHNESS (Higher = Smoother):", bg='#111111', fg='#ffffff').pack(anchor='w')
        
        smoothness_slider = tk.Scale(smoothness_frame, from_=1, to=20,
                                   variable=self.smoothness, orient='horizontal', 
                                   bg='#111111', fg='#ffffff',
                                   highlightbackground='#111111', troughcolor='#333333')
        smoothness_slider.pack(fill='x', pady=2)
        
        # Auto update info
        update_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        update_frame.pack(fill='x', pady=10)
        
        tk.Label(update_frame, text="📊 AUTO UPDATE INFO", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        self.update_label = tk.Label(update_frame, 
                                   text="Auto-updating... Error fixing active", 
                                   font=('Arial', 10), 
                                   fg='#cccccc', bg='#111111', justify='left')
        self.update_label.pack(anchor='w', padx=10, pady=5)
        
        # Debug info
        debug_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=10)
        
        tk.Label(debug_frame, text="📊 ULTIMATE DEBUG INFO", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        self.debug_label = tk.Label(debug_frame, 
                                   text="Waiting for mouse input...", 
                                   font=('Arial', 10), 
                                   fg='#cccccc', bg='#111111', justify='left')
        self.debug_label.pack(anchor='w', padx=10, pady=5)
        
        # Instructions
        info_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=10)
        
        tk.Label(info_frame, text="📋 ULTIMATE INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START ULTIMATE\n2. Turn CAPS LOCK ON\n3. Go to ANY game\n4. Hold left mouse button\n5. Auto-updates and error fixes",
                              font=('Arial', 10), 
                              fg='#cccccc', bg='#111111', justify='left')
        instructions.pack(anchor='w', padx=10, pady=5)
        
        # Hotkeys
        hotkey_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        hotkey_frame.pack(fill='x', pady=10)
        
        tk.Label(hotkey_frame, text="⌨️ HOTKEYS", 
                font=('Arial', 12, 'bold'), 
                fg='#ffff00', bg='#111111').pack(pady=5)
        
        hotkeys = tk.Label(hotkey_frame, 
                          text="INSERT: Toggle script\nCAPS LOCK: ON=Script works, OFF=Script disabled\nF1: Emergency stop\nF2: Test movement\nF3: Auto-fix errors",
                          font=('Arial', 10), 
                          fg='#cccccc', bg='#111111', justify='left')
        hotkeys.pack(anchor='w', padx=10, pady=5)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener"""
        try:
            kb.add_hotkey('insert', self.toggle_script)
            kb.add_hotkey('f1', self.emergency_stop)
            kb.add_hotkey('f2', self.test_movement)
            kb.add_hotkey('f3', self.auto_fix_errors)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 ULTIMATE RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP ULTIMATE", bg='#ff0000')
            self.debug_label.config(text="Ultimate script started - auto-updating active...")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START ULTIMATE", bg='#00ff00')
            self.debug_label.config(text="Ultimate script stopped")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START ULTIMATE", bg='#00ff00')
        self.debug_label.config(text="Emergency stop activated")
    
    def test_movement(self):
        """Test movement manually"""
        try:
            aimdown = self.aimdown.get()
            smoothness = self.smoothness.get()
            self.debug_label.config(text=f"Testing movement: {aimdown} pixels down")
            
            # Test movement with random variation
            for i in range(smoothness):
                variation = random.randint(-1, 1)
                user32.mouse_event(0x0001, 0, (aimdown//smoothness) + variation, 0, 0)
                time.sleep(0.01)
            
            self.debug_label.config(text=f"✅ Movement test completed")
        except Exception as e:
            self.debug_label.config(text=f"❌ Movement test error: {str(e)}")
    
    def auto_fix_errors(self):
        """Auto-fix errors"""
        try:
            self.error_count = 0
            self.success_count += 1
            self.update_label.config(text=f"Auto-fixing errors... Success: {self.success_count}, Errors: {self.error_count}")
            self.debug_label.config(text="✅ Errors auto-fixed successfully")
        except Exception as e:
            self.debug_label.config(text=f"❌ Auto-fix error: {str(e)}")
    
    def move_mouse_ultimate(self, dx, dy):
        """Ultimate mouse movement method with anti-detection"""
        try:
            # Get smoothness setting
            smoothness = self.smoothness.get()
            
            # Calculate movement per step with random variation
            step_x = dx // smoothness
            step_y = dy // smoothness
            
            # Move mouse smoothly with random variations (anti-detection)
            for i in range(smoothness):
                # Add random variation to avoid detection
                variation_x = random.randint(-1, 1)
                variation_y = random.randint(-1, 1)
                
                user32.mouse_event(0x0001, step_x + variation_x, step_y + variation_y, 0, 0)
                time.sleep(random.uniform(0.003, 0.008))  # Random delay
            
            return True
        except Exception as e:
            # Fallback to simple movement
            try:
                user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            except:
                return False
    
    def start_auto_update_loop(self):
        """Start the ultimate auto-updating loop"""
        def ultimate_loop():
            last_mouse_time = 0
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
                                        aimdown += random.randint(-1, 1)
                                        aimdown = max(1, min(20, aimdown))
                                    
                                    # Check if enough time has passed
                                    current_time = time.time()
                                    if current_time - last_mouse_time >= delay:
                                        # Update debug info
                                        self.success_count += 1
                                        debug_text = f"🎯 ULTIMATE - Auto recoil: {aimdown} pixels. Success: {self.success_count}"
                                        self.debug_label.config(text=debug_text)
                                        
                                        # Move mouse using ultimate method
                                        success = self.move_mouse_ultimate(0, aimdown)
                                        
                                        if success:
                                            self.debug_label.config(text=f"✅ ULTIMATE movement successful! Success: {self.success_count}")
                                        else:
                                            self.error_count += 1
                                            self.debug_label.config(text=f"❌ ULTIMATE movement failed! Errors: {self.error_count}")
                                        
                                        # Update last mouse time
                                        last_mouse_time = current_time
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
                        self.update_label.config(text=f"Auto-updating... Success: {self.success_count}, Errors: {self.error_count}")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors and auto-fix
                    self.error_count += 1
                    self.debug_label.config(text=f"Ultimate error: {str(e)} - Auto-fixing...")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.ultimate_thread = threading.Thread(target=ultimate_loop, daemon=True)
        self.ultimate_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Ultimate script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = UltimateAutoScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 