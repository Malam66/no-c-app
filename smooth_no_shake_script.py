import tkinter as tk
from tkinter import messagebox
import threading
import time
import sys
import ctypes
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

class SmoothNoShakeScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Smooth No-Shake Script")
        self.root.geometry("500x600")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.mouse_pressed = False
        self.test_count = 0
        self.last_mouse_time = 0
        
        # Variables
        self.aimdown = tk.IntVar(value=3)
        self.delay = tk.DoubleVar(value=0.05)
        self.smoothness = tk.IntVar(value=5)
        
        # Setup UI
        self.setup_ui()
        
        # Start the smooth loop immediately
        self.start_smooth_loop()
        
    def setup_ui(self):
        """Smooth no-shake UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 SMOOTH NO-SHAKE SCRIPT", 
                              font=('Arial', 16, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START SMOOTH", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Smooth control
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=10)
        
        tk.Label(control_frame, text="🎯 SMOOTH CONTROL", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
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
        
        # Debug info
        debug_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=10)
        
        tk.Label(debug_frame, text="📊 SMOOTH DEBUG INFO", 
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
        
        tk.Label(info_frame, text="📋 SMOOTH INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START SMOOTH\n2. Turn CAPS LOCK ON\n3. Go to your game\n4. Hold left mouse button\n5. CAPS OFF = Script disabled",
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
                          text="INSERT: Toggle script\nCAPS LOCK: ON=Script works, OFF=Script disabled\nF1: Emergency stop\nF2: Test smooth movement",
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
            kb.add_hotkey('f2', self.test_smooth_movement)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 SMOOTH RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP SMOOTH", bg='#ff0000')
            self.debug_label.config(text="Smooth script started - waiting for left mouse button...")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START SMOOTH", bg='#00ff00')
            self.debug_label.config(text="Smooth script stopped")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START SMOOTH", bg='#00ff00')
        self.debug_label.config(text="Emergency stop activated")
    
    def test_smooth_movement(self):
        """Test smooth mouse movement manually"""
        try:
            aimdown = self.aimdown.get()
            smoothness = self.smoothness.get()
            self.debug_label.config(text=f"Testing smooth movement: {aimdown} pixels down")
            
            # Test smooth movement
            for i in range(smoothness):
                user32.mouse_event(0x0001, 0, aimdown//smoothness, 0, 0)
                time.sleep(0.01)
            
            self.debug_label.config(text=f"✅ Smooth movement test completed")
        except Exception as e:
            self.debug_label.config(text=f"❌ Smooth movement error: {str(e)}")
    
    def move_mouse_smooth(self, dx, dy):
        """Smooth mouse movement method - no shaking"""
        try:
            # Get smoothness setting
            smoothness = self.smoothness.get()
            
            # Calculate movement per step
            step_x = dx // smoothness
            step_y = dy // smoothness
            
            # Move mouse smoothly in small steps
            for i in range(smoothness):
                user32.mouse_event(0x0001, step_x, step_y, 0, 0)
                time.sleep(0.005)  # Very small delay for smoothness
            
            return True
        except Exception as e:
            # Fallback to simple movement
            try:
                user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            except:
                return False
    
    def start_smooth_loop(self):
        """Start the smooth working loop"""
        def smooth_loop():
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
                            # Check if CAPS LOCK is ON (script only works when CAPS LOCK is ON)
                            try:
                                caps_lock_state = user32.GetKeyState(0x14)  # VK_CAPITAL
                                if caps_lock_state & 0x0001:  # CAPS LOCK is ON
                                    # Get current settings
                                    aimdown = self.aimdown.get()
                                    delay = self.delay.get()
                                    
                                    # Check if enough time has passed (prevents rapid firing)
                                    current_time = time.time()
                                    if current_time - self.last_mouse_time >= delay:
                                        # Update debug info
                                        self.test_count += 1
                                        debug_text = f"🎯 CAPS ON - Smooth recoil: {aimdown} pixels down. Count: {self.test_count}"
                                        self.debug_label.config(text=debug_text)
                                        
                                        # Move mouse using smooth method
                                        success = self.move_mouse_smooth(0, aimdown)
                                        
                                        if success:
                                            self.debug_label.config(text=f"✅ CAPS ON - Smooth movement successful! Count: {self.test_count}")
                                        else:
                                            self.debug_label.config(text=f"❌ CAPS ON - Smooth movement failed! Count: {self.test_count}")
                                        
                                        # Update last mouse time
                                        self.last_mouse_time = current_time
                                else:
                                    # CAPS LOCK is OFF - script doesn't work
                                    self.debug_label.config(text="🔴 CAPS LOCK OFF - Script disabled")
                            except:
                                # Fallback if CAPS LOCK detection fails
                                self.debug_label.config(text="⚠️ CAPS LOCK detection error")
                        else:
                            # Update debug when not pressing
                            self.debug_label.config(text="Waiting for left mouse button...")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors
                    self.debug_label.config(text=f"Smooth error: {str(e)}")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.smooth_thread = threading.Thread(target=smooth_loop, daemon=True)
        self.smooth_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Smooth script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = SmoothNoShakeScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 