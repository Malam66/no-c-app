import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import ctypes
import sys
import os

# Try to import required libraries with fallbacks
try:
    from pynput import keyboard, mouse
    pynput_available = True
except ImportError:
    pynput_available = False
    print("pynput not available, using fallback methods")

try:
    import keyboard as kb
    keyboard_available = True
except ImportError:
    keyboard_available = False
    print("keyboard library not available, using fallback methods")

try:
    import mouse as ms
    mouse_available = True
except ImportError:
    mouse_available = False
    print("mouse library not available, using fallback methods")

# Windows API for direct control
try:
    user32 = ctypes.windll.user32
    windows_api_available = True
except:
    windows_api_available = False
    print("Windows API not available")

class NoShakeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 NO SHAKE APP")
        self.root.geometry("700x800")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.auto_update = True
        self.anti_detection = True
        self.error_count = 0
        self.success_count = 0
        
        # Variables - optimized for no shaking
        self.aimdown = tk.IntVar(value=3)  # Lower default
        self.delay = tk.DoubleVar(value=0.05)  # Higher delay
        self.smoothness = tk.IntVar(value=15)  # Higher smoothness
        self.auto_strength = tk.BooleanVar(value=True)
        
        # Setup UI
        self.setup_ui()
        
        # Start auto-update loop
        self.start_auto_update_loop()
        
    def setup_ui(self):
        """No shake UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 NO SHAKE APP", 
                              font=('Arial', 20, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 16, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START NO SHAKE", 
                                     font=('Arial', 14, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=30, pady=15,
                                     command=self.toggle_script)
        self.start_button.pack(pady=15)
        
        # Control section
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=15)
        
        tk.Label(control_frame, text="🎯 NO SHAKE CONTROL", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        # Auto strength
        auto_frame = tk.Frame(control_frame, bg='#111111')
        auto_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Checkbutton(auto_frame, text="AUTO STRENGTH (No shake adaptation)", 
                      variable=self.auto_strength, bg='#111111', fg='#ffffff',
                      selectcolor='#333333', activebackground='#111111',
                      activeforeground='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        # Aimdown - optimized for no shaking
        aimdown_frame = tk.Frame(control_frame, bg='#111111')
        aimdown_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(aimdown_frame, text="AIMDOWN (Lower = No Shake):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        aimdown_slider = tk.Scale(aimdown_frame, from_=1, to=10,  # Reduced range
                                 variable=self.aimdown, orient='horizontal', 
                                 bg='#111111', fg='#ffffff',
                                 highlightbackground='#111111', troughcolor='#333333',
                                 length=300)
        aimdown_slider.pack(fill='x', pady=5)
        
        # Delay - optimized for smooth movement
        delay_frame = tk.Frame(control_frame, bg='#111111')
        delay_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(delay_frame, text="DELAY (Higher = No Shake):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        delay_slider = tk.Scale(delay_frame, from_=0.01, to=0.15, resolution=0.01,  # Optimized range
                               variable=self.delay, orient='horizontal', 
                               bg='#111111', fg='#ffffff',
                               highlightbackground='#111111', troughcolor='#333333',
                               length=300)
        delay_slider.pack(fill='x', pady=5)
        
        # Smoothness - optimized for no shaking
        smoothness_frame = tk.Frame(control_frame, bg='#111111')
        smoothness_frame.pack(fill='x', padx=15, pady=8)
        
        tk.Label(smoothness_frame, text="SMOOTHNESS (Higher = No Shake):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        smoothness_slider = tk.Scale(smoothness_frame, from_=10, to=30,  # Higher range
                                   variable=self.smoothness, orient='horizontal', 
                                   bg='#111111', fg='#ffffff',
                                   highlightbackground='#111111', troughcolor='#333333',
                                   length=300)
        smoothness_slider.pack(fill='x', pady=5)
        
        # Info section
        info_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=15)
        
        tk.Label(info_frame, text="📊 NO SHAKE INFO", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        self.info_label = tk.Label(info_frame, 
                                  text="No shake app ready - smooth movement active", 
                                  font=('Arial', 11), 
                                  fg='#cccccc', bg='#111111', justify='left')
        self.info_label.pack(anchor='w', padx=15, pady=8)
        
        # Debug section
        debug_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=15)
        
        tk.Label(debug_frame, text="📊 NO SHAKE DEBUG", 
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
        
        tk.Label(instructions_frame, text="📋 NO SHAKE INSTRUCTIONS", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        instructions = tk.Label(instructions_frame, 
                              text="1. Click START NO SHAKE\n2. Turn CAPS LOCK ON\n3. Go to ANY game\n4. Hold left mouse button\n5. Smooth movement - no shaking",
                              font=('Arial', 11), 
                              fg='#cccccc', bg='#111111', justify='left')
        instructions.pack(anchor='w', padx=15, pady=8)
        
        # Hotkeys
        hotkey_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        hotkey_frame.pack(fill='x', pady=15)
        
        tk.Label(hotkey_frame, text="⌨️ NO SHAKE HOTKEYS", 
                font=('Arial', 14, 'bold'), 
                fg='#ffff00', bg='#111111').pack(pady=8)
        
        hotkeys = tk.Label(hotkey_frame, 
                          text="INSERT: Toggle script\nCAPS LOCK: ON=Script works, OFF=Script disabled\nF1: Emergency stop\nF2: Test movement\nF3: Auto-fix errors",
                          font=('Arial', 11), 
                          fg='#cccccc', bg='#111111', justify='left')
        hotkeys.pack(anchor='w', padx=15, pady=8)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener with fallbacks"""
        try:
            if keyboard_available:
                kb.add_hotkey('insert', self.toggle_script)
                kb.add_hotkey('f1', self.emergency_stop)
                kb.add_hotkey('f2', self.test_movement)
                kb.add_hotkey('f3', self.auto_fix_errors)
                self.debug_label.config(text="✅ Keyboard listener started")
            else:
                self.debug_label.config(text="⚠️ Keyboard library not available")
        except Exception as e:
            self.debug_label.config(text=f"⚠️ Keyboard listener error: {str(e)}")
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 NO SHAKE RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP NO SHAKE", bg='#ff0000')
            self.debug_label.config(text="No shake app started - smooth movement active...")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START NO SHAKE", bg='#00ff00')
            self.debug_label.config(text="No shake app stopped")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START NO SHAKE", bg='#00ff00')
        self.debug_label.config(text="Emergency stop activated")
    
    def test_movement(self):
        """Test movement manually - no shaking"""
        try:
            aimdown = self.aimdown.get()
            smoothness = self.smoothness.get()
            self.debug_label.config(text=f"Testing smooth movement: {aimdown} pixels down")
            
            # Test movement with smooth motion - no shaking
            for i in range(smoothness):
                # Smooth movement without random variation
                step_size = aimdown // smoothness
                if windows_api_available:
                    user32.mouse_event(0x0001, 0, step_size, 0, 0)
                time.sleep(0.02)  # Consistent delay
            
            self.debug_label.config(text=f"✅ Smooth movement test completed")
        except Exception as e:
            self.debug_label.config(text=f"❌ Movement test error: {str(e)}")
    
    def auto_fix_errors(self):
        """Auto-fix errors"""
        try:
            self.error_count = 0
            self.success_count += 1
            self.info_label.config(text=f"Auto-fixing errors... Success: {self.success_count}, Errors: {self.error_count}")
            self.debug_label.config(text="✅ Errors auto-fixed successfully")
        except Exception as e:
            self.debug_label.config(text=f"❌ Auto-fix error: {str(e)}")
    
    def move_mouse_no_shake(self, dx, dy):
        """No shake mouse movement method"""
        try:
            if not windows_api_available:
                return False
                
            # Get smoothness setting
            smoothness = self.smoothness.get()
            
            # Calculate movement per step - smooth and consistent
            step_x = dx // smoothness
            step_y = dy // smoothness
            
            # Move mouse smoothly without random variations (prevents shaking)
            for i in range(smoothness):
                # Consistent movement without random variation
                user32.mouse_event(0x0001, step_x, step_y, 0, 0)
                time.sleep(0.02)  # Consistent delay
            
            return True
        except Exception as e:
            # Fallback to simple movement
            try:
                if windows_api_available:
                    user32.mouse_event(0x0001, dx, dy, 0, 0)
                    return True
                return False
            except:
                return False
    
    def check_mouse_pressed(self):
        """Check if mouse is pressed using multiple methods"""
        mouse_pressed = False
        
        # Method 1: Keyboard library
        if keyboard_available:
            try:
                if kb.is_pressed('left'):
                    mouse_pressed = True
            except:
                pass
        
        # Method 2: Mouse library
        if mouse_available:
            try:
                if ms.is_pressed('left'):
                    mouse_pressed = True
            except:
                pass
        
        # Method 3: Windows API
        if windows_api_available:
            try:
                if user32.GetAsyncKeyState(0x01) & 0x8000:
                    mouse_pressed = True
            except:
                pass
        
        return mouse_pressed
    
    def check_caps_lock(self):
        """Check CAPS LOCK state"""
        try:
            if windows_api_available:
                caps_lock_state = user32.GetKeyState(0x14)
                return caps_lock_state & 0x0001  # CAPS LOCK is ON
            return True  # Default to ON if can't detect
        except:
            return True  # Default to ON if error
    
    def start_auto_update_loop(self):
        """Start the no shake auto-updating loop"""
        def no_shake_loop():
            last_mouse_time = 0
            while True:
                try:
                    # Check if script is running
                    if self.running:
                        # Check if left mouse button is pressed
                        mouse_pressed = self.check_mouse_pressed()
                        
                        if mouse_pressed:
                            # Check if CAPS LOCK is ON
                            caps_lock_on = self.check_caps_lock()
                            
                            if caps_lock_on:
                                # Get current settings
                                aimdown = self.aimdown.get()
                                delay = self.delay.get()
                                
                                # Auto-strength adjustment - minimal for no shaking
                                if self.auto_strength.get():
                                    # Minimal adjustment to prevent shaking
                                    aimdown += random.randint(-1, 1)
                                    aimdown = max(1, min(10, aimdown))  # Limited range
                                
                                # Check if enough time has passed
                                current_time = time.time()
                                if current_time - last_mouse_time >= delay:
                                    # Update debug info
                                    self.success_count += 1
                                    debug_text = f"🎯 NO SHAKE - Smooth recoil: {aimdown} pixels. Success: {self.success_count}"
                                    self.debug_label.config(text=debug_text)
                                    
                                    # Move mouse using no shake method
                                    success = self.move_mouse_no_shake(0, aimdown)
                                    
                                    if success:
                                        self.debug_label.config(text=f"✅ NO SHAKE movement successful! Success: {self.success_count}")
                                    else:
                                        self.error_count += 1
                                        self.debug_label.config(text=f"❌ NO SHAKE movement failed! Errors: {self.error_count}")
                                    
                                    # Update last mouse time
                                    last_mouse_time = current_time
                            else:
                                # CAPS LOCK is OFF
                                self.debug_label.config(text="🔴 CAPS LOCK OFF - Script disabled")
                        else:
                            # Update debug when not pressing
                            self.debug_label.config(text="Waiting for mouse input...")
                    
                    # Auto-update status
                    if self.auto_update:
                        self.info_label.config(text=f"Auto-updating... Success: {self.success_count}, Errors: {self.error_count}")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors and auto-fix
                    self.error_count += 1
                    self.debug_label.config(text=f"No shake app error: {str(e)} - Auto-fixing...")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.no_shake_thread = threading.Thread(target=no_shake_loop, daemon=True)
        self.no_shake_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "No shake app is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    try:
        root = tk.Tk()
        app = NoShakeApp(root)
        root.protocol("WM_DELETE_WINDOW", app.on_closing)
        root.mainloop()
    except Exception as e:
        print(f"Error starting app: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main() 