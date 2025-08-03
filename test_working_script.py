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

class TestWorkingScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Test Working Script")
        self.root.geometry("500x600")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.test_count = 0
        
        # Variables
        self.strength = tk.IntVar(value=5)
        self.delay = tk.DoubleVar(value=0.02)
        
        # Setup UI
        self.setup_ui()
        
        # Start the test loop immediately
        self.start_test_loop()
        
    def setup_ui(self):
        """Test working UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 TEST WORKING SCRIPT", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff0000', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START TEST", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#ff0000', fg='#ffffff',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Test control
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=10)
        
        tk.Label(control_frame, text="🧪 TEST CONTROL", 
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
        
        tk.Label(debug_frame, text="📊 DEBUG INFO", 
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
        
        tk.Label(info_frame, text="📋 TEST INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START TEST\n2. Go to your game\n3. Hold left mouse button\n4. Watch debug info\n5. Multiple mouse methods tested",
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
                          text="INSERT: Toggle script\nF1: Emergency stop\nF2: Test mouse movement",
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
            kb.add_hotkey('f2', self.test_mouse_movement)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 TEST RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP TEST", bg='#00ff00')
            self.debug_label.config(text="Script started - waiting for left mouse button...")
            messagebox.showinfo("TEST STARTED", "Test script is running!\nGo to your game and hold left mouse button.\nWatch debug info for details!")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START TEST", bg='#ff0000')
            self.debug_label.config(text="Script stopped")
            messagebox.showinfo("Stopped", "Test script stopped.")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START TEST", bg='#ff0000')
        self.debug_label.config(text="Emergency stop activated")
    
    def test_mouse_movement(self):
        """Test mouse movement manually"""
        try:
            strength = self.strength.get()
            self.debug_label.config(text=f"Testing mouse movement: {strength} pixels down")
            
            # Test multiple methods
            # Method 1: Windows API
            user32.mouse_event(0x0001, 0, strength, 0, 0)
            time.sleep(0.1)
            
            # Method 2: Mouse library
            ms.move(0, strength, absolute=False)
            time.sleep(0.1)
            
            # Method 3: Direct ctypes
            ctypes.windll.user32.mouse_event(0x0001, 0, strength, 0, 0)
            
            self.debug_label.config(text=f"Mouse test completed: {strength} pixels moved")
        except Exception as e:
            self.debug_label.config(text=f"Mouse test error: {str(e)}")
    
    def move_mouse_test(self, dx, dy):
        """Test multiple mouse movement methods"""
        try:
            # Method 1: Windows API
            user32.mouse_event(0x0001, dx, dy, 0, 0)
            return True
        except:
            try:
                # Method 2: Mouse library
                ms.move(dx, dy, absolute=False)
                return True
            except:
                try:
                    # Method 3: Direct ctypes
                    ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 0)
                    return True
                except:
                    return False
    
    def start_test_loop(self):
        """Start the test working loop"""
        def test_loop():
            while True:
                try:
                    # Check if script is running
                    if self.running:
                        # Check if left mouse button is pressed
                        if kb.is_pressed('left'):
                            # Get current settings
                            strength = self.strength.get()
                            delay = self.delay.get()
                            
                            # Update debug info
                            self.test_count += 1
                            debug_text = f"Mouse pressed! Moving {strength} pixels down. Count: {self.test_count}"
                            self.debug_label.config(text=debug_text)
                            
                            # Move mouse using test method
                            success = self.move_mouse_test(0, strength)
                            
                            if success:
                                self.debug_label.config(text=f"✅ Mouse moved successfully! Count: {self.test_count}")
                            else:
                                self.debug_label.config(text=f"❌ Mouse movement failed! Count: {self.test_count}")
                            
                            time.sleep(delay)
                        else:
                            # Update debug when not pressing
                            self.debug_label.config(text="Waiting for left mouse button...")
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors
                    self.debug_label.config(text=f"Error: {str(e)}")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.test_thread = threading.Thread(target=test_loop, daemon=True)
        self.test_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Test script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = TestWorkingScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 