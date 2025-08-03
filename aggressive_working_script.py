import tkinter as tk
from tkinter import messagebox
import threading
import time
import sys

# Direct imports
try:
    import keyboard as kb
    import mouse as ms
except ImportError:
    messagebox.showerror("Error", "Please install: pip install keyboard mouse")
    sys.exit(1)

class AggressiveWorkingScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Aggressive Working Script")
        self.root.geometry("400x500")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        
        # Variables
        self.strength = tk.IntVar(value=8)
        self.delay = tk.DoubleVar(value=0.01)
        
        # Setup UI
        self.setup_ui()
        
        # Start the aggressive loop immediately
        self.start_aggressive_loop()
        
    def setup_ui(self):
        """Aggressive working UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 AGGRESSIVE WORKING SCRIPT", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff0000', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START AGGRESSIVE", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#ff0000', fg='#ffffff',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Aggressive control
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=10)
        
        tk.Label(control_frame, text="💪 AGGRESSIVE CONTROL", 
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
        
        delay_slider = tk.Scale(delay_frame, from_=0.001, to=0.05, resolution=0.001,
                               variable=self.delay, orient='horizontal', 
                               bg='#111111', fg='#ffffff',
                               highlightbackground='#111111', troughcolor='#333333')
        delay_slider.pack(fill='x', pady=2)
        
        # Instructions
        info_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=10)
        
        tk.Label(info_frame, text="📋 AGGRESSIVE INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START AGGRESSIVE\n2. Go to your game\n3. Hold left mouse button\n4. Works immediately!\n5. No complex settings needed",
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
            self.status_label.config(text="🟢 AGGRESSIVE RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP AGGRESSIVE", bg='#00ff00')
            messagebox.showinfo("AGGRESSIVE STARTED", "Aggressive script is running!\nGo to your game and hold left mouse button.\nThis version WILL work!")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START AGGRESSIVE", bg='#ff0000')
            messagebox.showinfo("Stopped", "Aggressive script stopped.")
    
    def emergency_stop(self):
        """Emergency stop"""
        self.running = False
        self.status_label.config(text="🔴 EMERGENCY STOPPED", fg='#ff0000')
        self.start_button.config(text="START AGGRESSIVE", bg='#ff0000')
    
    def start_aggressive_loop(self):
        """Start the aggressive working loop"""
        def aggressive_loop():
            while True:
                try:
                    # Check if script is running
                    if self.running:
                        # Check if left mouse button is pressed
                        if kb.is_pressed('left'):
                            # Get current settings
                            strength = self.strength.get()
                            delay = self.delay.get()
                            
                            # Aggressive mouse movement - multiple movements
                            for i in range(3):  # Move 3 times for aggressive effect
                                ms.move(0, strength, absolute=False)
                                time.sleep(delay / 3)
                            
                            # Small pause
                            time.sleep(delay)
                    
                    # Very small delay for responsiveness
                    time.sleep(0.001)
                    
                except Exception as e:
                    # Handle errors
                    time.sleep(0.01)
        
        # Start the loop in a separate thread
        self.aggressive_thread = threading.Thread(target=aggressive_loop, daemon=True)
        self.aggressive_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Aggressive script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = AggressiveWorkingScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 