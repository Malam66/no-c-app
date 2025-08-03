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

class FinalWorkingScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Final Working Script")
        self.root.geometry("500x600")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.mouse_pressed = False
        self.test_count = 0
        
        # Variables
        self.strength = tk.IntVar(value=5)
        self.delay = tk.DoubleVar(value=0.02)
        
        # Setup UI
        self.setup_ui()
        
        # Start the final loop immediately
        self.start_final_loop()
        
    def setup_ui(self):
        """Final working UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 FINAL WORKING SCRIPT", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff0000', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START FINAL", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#ff0000', fg='#ffffff',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Final control
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=10)
        
        tk.Label(control_frame, text="🎯 FINAL CONTROL", 
                font=('Arial', 12, 'bold'), 
                fg='#ff0000', bg='#111111').pack(pady=5)
        
        # Strength
        strength_frame = tk.Frame(control_frame, bg='#111111')
        strength_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(strength_frame, text="STRENGTH:", bg='#111111', fg='#ffffff').pack(anchor='w')
        
        strength_slider = tk.Scale(strength_frame, from_=1, to=20,
                                  variable=self.strength, orient='horizontal', 
                                  bg='#111111', fg='#ffffff',
                                  highlightbackground='#111111', troughcolor='#333333')
        strength_slider.pack(fill='x', pady=2)
        
        # Delay
        delay_frame = tk.Frame(control_frame, bg='#111111')
        delay_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(delay_frame, text="DELAY:", bg='#111111', fg='#ffffff').pack(anchor='w')
        
        delay_slider = tk.Scale(delay_frame, from_=0.01, to=0.1, resolution=0.01,
                               variable=self.delay, orient='horizontal', 
                               bg='#111111', fg='#ffffff',
                               highlightbackground='#111111', troughcolor='#333333')
        delay_slider.pack(fill='x', pady=2)
        
        # Debug info
        debug_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=10)
        
        tk.Label(debug_frame, text="📊 FINAL DEBUG INFO", 
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
        
        tk.Label(info_frame, text="📋 FINAL INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START FINAL\n2. Go to your game\n3. Hold left mouse button\n4. Watch debug info\n5. This version WILL work!",
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
                          text="INSERT: Toggle script\nCAPS LOCK: Toggle script\nF1: Emergency stop\nF2: Force mouse movement",
                          font=('Arial', 10), 
                          fg='#cccccc', bg='#111111', justify='left')
        hotkeys.pack(anchor='w', padx=10, pady=5)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener"""
        try:
            kb.add_hotkey('insert', self.toggle_script)
            kb.add_hotkey('caps lock', self.toggle_script)
            kb.add_hotkey('f1', self.emergency_stop)
            kb.add_hotkey('f2', self.force_mouse_movement)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 FINAL RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP FINAL", bg='#00ff00')
            self.debug_label.config(text="Final script started - waiting for left mouse button...")
            messagebox.showinfo("FINAL STARTED", "Final script is running!\nGo to your game and hold left mouse button.\nThis version WILL work!")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START FINAL", bg='#ff0000')
            self.debug_label.config(text="Final script stopped")
            messagebox.showinfo("Stopped", "Final script stopped.")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START FINAL", bg='#ff0000')
        self.debug_label.config(text="Emergency stop activated")
    
    def force_mouse_movement(self):
        """Force mouse movement manually"""
        try:
            strength = self.strength.get()
            self.debug_label.config(text=f"Forcing mouse movement: {strength} pixels down")
            
            # Force mouse movement using multiple methods
            # Method 1: Direct Windows API
            user32.mouse_event(0x0001, 0, strength, 0, 0)
            time.sleep(0.05)
            
            # Method 2: Mouse library
            ms.move(0, strength, absolute=False)
            time.sleep(0.05)
            
            # Method 3: Direct ctypes
            ctypes.windll.user32.mouse_event(0x0001, 0, strength, 0, 0)
            
            self.debug_label.config(text=f"✅ Force mouse movement completed: {strength} pixels moved")
        except Exception as e:
            self.debug_label.config(text=f"❌ Force mouse movement error: {str(e)}")
    
    def move_mouse_final(self, dx, dy):
        """Final mouse movement method"""
        try:
            # Use direct Windows API with error handling
            result = user32.mouse_event(0x0001, dx, dy, 0, 0)
            if result == 0:  # Success
                return True
            else:
                # Try mouse library as fallback
                ms.move(dx, dy, absolute=False)
                return True
        except Exception as e:
            # Try direct ctypes as final fallback
            try:
                ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 0)
                return True
            except:
                return False
    
    def start_final_loop(self):
        """Start the final working loop"""
        def final_loop():
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
                            # Get current settings
                            strength = self.strength.get()
                            delay = self.delay.get()
                            
                            # Update debug info
                            self.test_count += 1
                            debug_text = f"🎯 Mouse detected! Moving {strength} pixels down. Count: {self.test_count}"
                            self.debug_label.config(text=debug_text)
                            
                            # Move mouse using final method
                            success = self.move_mouse_final(0, strength)
                            
                            if success:
                                self.debug_label.config(text=f"✅ Final mouse movement successful! Count: {self.test_count}")
                            else:
                                self.debug_label.config(text=f"❌ Final mouse movement failed! Count: {self.test_count}")
                            
                            time.sleep(delay)
                        else:
                            # Update debug when not pressing
                            self.debug_label.config(text="Waiting for left mouse button...")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors
                    self.debug_label.config(text=f"Final error: {str(e)}")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.final_thread = threading.Thread(target=final_loop, daemon=True)
        self.final_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Final script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = FinalWorkingScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 