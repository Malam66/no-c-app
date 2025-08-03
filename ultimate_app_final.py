import tkinter as tk
from tkinter import messagebox
import threading
import time
import random
import ctypes
from pynput import keyboard, mouse
import keyboard as kb
import mouse as ms

# Windows API for direct control
user32 = ctypes.windll.user32

def create_desktop_shortcut():
    """Create desktop shortcut"""
    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        shortcut_path = os.path.join(desktop, "Ultimate Anti-Recoil App.lnk")
        
        # Create shortcut using PowerShell
        ps_command = f'$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut("{shortcut_path}"); $Shortcut.TargetPath = "{sys.executable}"; $Shortcut.WorkingDirectory = "{os.getcwd()}"; $Shortcut.Description = "Ultimate Anti-Recoil App"; $Shortcut.Save()'
        
        subprocess.run(["powershell", "-Command", ps_command], capture_output=True)
        return True
    except:
        return False

class UltimateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ULTIMATE ANTI-RECOIL APP")
        self.root.geometry("700x800")
        self.root.configure(bg='#000000')
        self.root.resizable(False, False)
        
        # App state
        self.running = False
        self.error_count = 0
        self.success_count = 0
        
        # Variables
        self.aimdown = tk.IntVar(value=5)
        self.delay = tk.DoubleVar(value=0.03)
        self.auto_strength = tk.BooleanVar(value=True)
        
        # Setup UI
        self.setup_ui()
        
        # Create desktop shortcut
        if create_desktop_shortcut():
            print("Desktop shortcut created successfully!")
        
        # Start auto-update loop
        self.start_auto_update_loop()
        
    def setup_ui(self):
        """Setup the UI"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000', padx=20, pady=20)
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="ULTIMATE ANTI-RECOIL APP", 
                              font=('Arial', 20, 'bold'), 
                              fg='#00ff00', bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Status
        self.status_label = tk.Label(main_frame, text="STOPPED", 
                                    font=('Arial', 16, 'bold'),
                                    fg='#ff0000', bg='#000000')
        self.status_label.pack(pady=10)
        
        # Start button
        self.start_button = tk.Button(main_frame, text="START ULTIMATE APP", 
                                     font=('Arial', 14, 'bold'),
                                     bg='#00ff00', fg='#000000',
                                     relief='flat', padx=30, pady=15,
                                     command=self.toggle_script)
        self.start_button.pack(pady=15)
        
        # Control section
        control_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        control_frame.pack(fill='x', pady=15)
        
        tk.Label(control_frame, text="ULTIMATE APP CONTROL", 
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
        
        tk.Label(delay_frame, text="DELAY (Seconds):", bg='#111111', fg='#ffffff', font=('Arial', 11)).pack(anchor='w')
        
        delay_slider = tk.Scale(delay_frame, from_=0.01, to=0.1,
                               variable=self.delay, orient='horizontal', 
                               bg='#111111', fg='#ffffff',
                               highlightbackground='#111111', troughcolor='#333333',
                               length=300, resolution=0.01)
        delay_slider.pack(fill='x', pady=5)
        
        # Info section
        info_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        info_frame.pack(fill='x', pady=15)
        
        tk.Label(info_frame, text="STATUS INFO", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        self.info_label = tk.Label(info_frame, text="Ready to start...", 
                                  font=('Arial', 11), 
                                  fg='#ffffff', bg='#111111')
        self.info_label.pack(pady=5)
        
        self.debug_label = tk.Label(info_frame, text="Waiting for input...", 
                                   font=('Arial', 10), 
                                   fg='#cccccc', bg='#111111')
        self.debug_label.pack(pady=5)
        
        # Instructions
        instructions_frame = tk.Frame(main_frame, bg='#111111', relief='raised', bd=2)
        instructions_frame.pack(fill='x', pady=15)
        
        tk.Label(instructions_frame, text="INSTRUCTIONS", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        instructions = [
            "1. Click 'START ULTIMATE APP'",
            "2. Turn ON CAPS LOCK to enable",
            "3. Hold left mouse button while aiming",
            "4. Turn OFF CAPS LOCK to disable",
            "5. Adjust settings as needed"
        ]
        
        for instruction in instructions:
            tk.Label(instructions_frame, text=instruction, 
                    font=('Arial', 10), 
                    fg='#ffffff', bg='#111111').pack(anchor='w', padx=15)
    
    def toggle_script(self):
        """Toggle the script on/off"""
        if not self.running:
            self.running = True
            self.status_label.config(text="RUNNING", fg='#00ff00')
            self.start_button.config(text="STOP ULTIMATE APP", bg='#ff0000')
            self.info_label.config(text="App is running! Turn on CAPS LOCK to enable.")
        else:
            self.running = False
            self.status_label.config(text="STOPPED", fg='#ff0000')
            self.start_button.config(text="START ULTIMATE APP", bg='#00ff00')
            self.info_label.config(text="App stopped.")
    
    def move_mouse(self, dx, dy):
        """Move mouse by delta"""
        try:
            user32.mouse_event(0x0001, dx, dy, 0, 0)
            return True
        except:
            return False
    
    def start_auto_update_loop(self):
        """Start the auto-update loop"""
        def update_loop():
            last_mouse_time = 0
            
            while True:
                try:
                    if self.running:
                        # Check if left mouse button is pressed
                        mouse_pressed = False
                        
                        try:
                            if kb.is_pressed('left') or ms.is_pressed('left'):
                                mouse_pressed = True
                        except:
                            pass
                        
                        if mouse_pressed:
                            # Check if CAPS LOCK is ON
                            try:
                                caps_lock_state = user32.GetKeyState(0x14)
                                if caps_lock_state & 0x0001:  # CAPS LOCK is ON
                                    aimdown = self.aimdown.get()
                                    delay = self.delay.get()
                                    
                                    # Auto-strength adjustment
                                    if self.auto_strength.get():
                                        aimdown += random.randint(-2, 2)
                                        aimdown = max(1, min(25, aimdown))
                                    
                                    current_time = time.time()
                                    if current_time - last_mouse_time >= delay:
                                        self.success_count += 1
                                        self.debug_label.config(text=f"Anti-recoil: {aimdown}px. Success: {self.success_count}")
                                        
                                        if self.move_mouse(0, aimdown):
                                            self.debug_label.config(text=f"Movement successful! Success: {self.success_count}")
                                        else:
                                            self.error_count += 1
                                            self.debug_label.config(text=f"Movement failed! Errors: {self.error_count}")
                                        
                                        last_mouse_time = current_time
                                else:
                                    self.debug_label.config(text="CAPS LOCK OFF - Script disabled")
                            except:
                                self.debug_label.config(text="CAPS LOCK detection error")
                        else:
                            self.debug_label.config(text="Waiting for mouse input...")
                    
                    # Auto-update status
                    self.info_label.config(text=f"Auto-updating... Success: {self.success_count}, Errors: {self.error_count}")
                    
                    time.sleep(0.01)
                    
                except Exception as e:
                    self.error_count += 1
                    self.debug_label.config(text=f"Error: {str(e)} - Auto-fixing...")
                    time.sleep(0.1)
        
        # Start the loop in a separate thread
        self.update_thread = threading.Thread(target=update_loop, daemon=True)
        self.update_thread.start()

def main():
    """Main function"""
    root = tk.Tk()
    app = UltimateApp(root)
    
    def on_closing():
        if app.running:
            if messagebox.askokcancel("Quit", "App is running. Quit?"):
                root.destroy()
        else:
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
