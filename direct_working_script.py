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

class DirectWorkingScript:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Direct Working Script")
        self.root.geometry("400x500")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.recoil_enabled = False
        
        # Variables
        self.strength = tk.IntVar(value=5)
        self.delay = tk.DoubleVar(value=0.02)
        
        # Setup UI
        self.setup_ui()
        
        # Start the working loop immediately
        self.start_working_loop()
        
    def setup_ui(self):
        """Simple working UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🎯 DIRECT WORKING SCRIPT", 
                              font=('Arial', 16, 'bold'), 
                              fg='#ff0000', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="🔴 STOPPED", 
                                    font=('Arial', 14, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START SCRIPT", 
                                     font=('Arial', 12, 'bold'),
                                     bg='#ff0000', fg='#ffffff',
                                     relief='flat', padx=20, pady=10,
                                     command=self.toggle_script)
        self.start_button.pack(pady=10)
        
        # Recoil control
        recoil_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        recoil_frame.pack(fill='x', pady=10)
        
        tk.Label(recoil_frame, text="🔫 RECOIL CONTROL", 
                font=('Arial', 12, 'bold'), 
                fg='#ff0000', bg='#111111').pack(pady=5)
        
        # Enable recoil
        self.recoil_var = tk.BooleanVar(value=False)
        tk.Checkbutton(recoil_frame, text="ENABLE RECOIL", 
                      variable=self.recoil_var, bg='#111111', fg='#ffffff',
                      selectcolor='#333333', activebackground='#111111',
                      activeforeground='#ffffff').pack(anchor='w', padx=10, pady=2)
        
        # Strength
        strength_frame = tk.Frame(recoil_frame, bg='#111111')
        strength_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(strength_frame, text="STRENGTH:", bg='#111111', fg='#ffffff').pack(anchor='w')
        
        strength_slider = tk.Scale(strength_frame, from_=1, to=10,
                                  variable=self.strength, orient='horizontal', 
                                  bg='#111111', fg='#ffffff',
                                  highlightbackground='#111111', troughcolor='#333333')
        strength_slider.pack(fill='x', pady=2)
        
        # Delay
        delay_frame = tk.Frame(recoil_frame, bg='#111111')
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
        
        tk.Label(info_frame, text="📋 INSTRUCTIONS", 
                font=('Arial', 12, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=5)
        
        instructions = tk.Label(info_frame, 
                              text="1. Click START\n2. Enable recoil\n3. Go to game\n4. Hold left mouse\n5. Works immediately!",
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
                          text="INSERT: Toggle script\nF1: Toggle recoil",
                          font=('Arial', 10), 
                          fg='#cccccc', bg='#111111', justify='left')
        hotkeys.pack(anchor='w', padx=10, pady=5)
        
        # Start keyboard listener
        self.start_keyboard_listener()
        
    def start_keyboard_listener(self):
        """Start keyboard listener"""
        try:
            kb.add_hotkey('insert', self.toggle_script)
            kb.add_hotkey('f1', self.toggle_recoil)
        except:
            pass
        
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="🟢 RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP SCRIPT", bg='#00ff00')
            messagebox.showinfo("Started", "Direct script is running!\nGo to your game and hold left mouse button.")
        else:
            self.running = False
            self.status_label.config(text="🔴 STOPPED", fg='#ff0000')
            self.start_button.config(text="START SCRIPT", bg='#ff0000')
            messagebox.showinfo("Stopped", "Direct script stopped.")
    
    def toggle_recoil(self):
        """Toggle recoil on/off"""
        if self.recoil_var.get():
            self.recoil_var.set(False)
        else:
            self.recoil_var.set(True)
    
    def start_working_loop(self):
        """Start the direct working loop"""
        def working_loop():
            while True:
                try:
                    # Check if script is running and recoil is enabled
                    if self.running and self.recoil_var.get():
                        # Check if left mouse button is pressed
                        if kb.is_pressed('left'):
                            # Get current settings
                            strength = self.strength.get()
                            delay = self.delay.get()
                            
                            # Direct mouse movement
                            ms.move(0, strength, absolute=False)
                            time.sleep(delay)
                    
                    # Small delay
                    time.sleep(0.01)
                    
                except Exception as e:
                    # Handle errors
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.working_thread = threading.Thread(target=working_loop, daemon=True)
        self.working_thread.start()
    
    def on_closing(self):
        """Handle closing"""
        if self.running:
            if messagebox.askokcancel("Quit", "Script is running. Quit?"):
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    root = tk.Tk()
    app = DirectWorkingScript(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 