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

class SimpleWorkingScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Simple Working Script")
        self.root.geometry("400x500")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        
        # Variables
        self.strength = tk.IntVar(value=10)
        self.delay = tk.DoubleVar(value=0.02)
        
        # Setup UI
        self.setup_ui()
        
        # Start the simple loop immediately
        self.start_simple_loop()
        
    def setup_ui(self):
        """Simple working UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 SIMPLE WORKING SCRIPT", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff0000', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START SIMPLE", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#ff0000', fg='#ffffff',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Simple control
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=10)
        
        tk.Label(control_frame, text="🎯 SIMPLE CONTROL", 
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
        
        # Instructions
        info_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=10)
        
        tk.Label(info_frame, text="📋 SIMPLE INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START SIMPLE\n2. Go to your game\n3. Hold left mouse button\n4. Works immediately!\n5. Uses direct Windows API",
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
                          text="INSERT: Toggle script\nF1: Emergency stop",
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
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 SIMPLE RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP SIMPLE", bg='#00ff00')
            messagebox.showinfo("SIMPLE STARTED", "Simple script is running!\nGo to your game and hold left mouse button.\nUses direct Windows API!")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START SIMPLE", bg='#ff0000')
            messagebox.showinfo("Stopped", "Simple script stopped.")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START SIMPLE", bg='#ff0000')
    
    def move_mouse_direct(self, dx, dy):
        """Move mouse using direct Windows API"""
        try:
            # Use Windows API for direct mouse movement
            user32.mouse_event(0x0001, dx, dy, 0, 0)  # MOUSEEVENTF_MOVE
        except:
            # Fallback to mouse library
            try:
                ms.move(dx, dy, absolute=False)
            except:
                pass
    
    def start_simple_loop(self):
        """Start the simple working loop"""
        def simple_loop():
            while True:
                try:
                    # Check if script is running
                    if self.running:
                        # Check if left mouse button is pressed
                        if kb.is_pressed('left'):
                            # Get current settings
                            strength = self.strength.get()
                            delay = self.delay.get()
                            
                            # Move mouse using direct API
                            self.move_mouse_direct(0, strength)
                            time.sleep(delay)
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.simple_thread = threading.Thread(target=simple_loop, daemon=True)
        self.simple_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Simple script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = SimpleWorkingScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 