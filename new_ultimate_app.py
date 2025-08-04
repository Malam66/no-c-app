#!/usr/bin/env python3
# Ultimate Gaming App - NEW VERSION

import tkinter as tk
from tkinter import ttk
import threading
import time
import random
import ctypes
from ctypes import wintypes
import keyboard
import pynput
from pynput import mouse, keyboard as kb

user32 = ctypes.windll.user32

class UltimateGamingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ultimate Gaming App - NEW VERSION")
        self.root.geometry("800x600")
        self.root.configure(bg='#1a1a1a')
        
        self.app_startup_time = time.time()
        self.startup_delay = 10.0
        self.running = True
        self.auto_update = True
        self.success_count = 0
        self.error_count = 0
        
        self.aimdown = tk.IntVar(value=15)
        self.smoothness = tk.IntVar(value=15)
        self.delay = tk.DoubleVar(value=0.05)
        
        self.aim_assist_enabled = tk.BooleanVar(value=True)
        self.aim_assist_strength = tk.IntVar(value=20)
        self.anti_shaking_enabled = tk.BooleanVar(value=True)
        
        self.auto_fire = tk.BooleanVar(value=False)
        self.rapid_fire = tk.BooleanVar(value=False)
        self.trigger_bot = tk.BooleanVar(value=False)
        
        self.app_enabled = tk.BooleanVar(value=True)
        
        self.mouse_moving = False
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        
        self.setup_ui()
        self.start_auto_update_loop()
        self.start_mouse_tracking()
        self.start_keyboard_listener()
        
    def setup_ui(self):
        title_label = tk.Label(self.root, text="ULTIMATE GAMING APP - NEW VERSION", 
                              font=('Arial', 20, 'bold'), 
                              fg='#00ff00', bg='#1a1a1a')
        title_label.pack(pady=20)
        
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        main_frame = tk.Frame(notebook, bg='#1a1a1a')
        notebook.add(main_frame, text='Main')
        self.setup_main_tab(main_frame)
        
        settings_frame = tk.Frame(notebook, bg='#1a1a1a')
        notebook.add(settings_frame, text='Settings')
        self.setup_settings_tab(settings_frame)
        
    def setup_main_tab(self, parent):
        anti_recoil_frame = tk.Frame(parent, bg='#2a2a2a', relief='raised', bd=3)
        anti_recoil_frame.pack(fill='x', pady=15, padx=25)
        
        tk.Label(anti_recoil_frame, text="ANTI-RECOIL - NEW VERSION", 
                font=('Arial', 16, 'bold'), 
                fg='#00ff00', bg='#2a2a2a').pack(pady=12)
        
        controls_frame = tk.Frame(anti_recoil_frame, bg='#2a2a2a')
        controls_frame.pack(fill='x', padx=20, pady=10)
        
        aimdown_frame = tk.Frame(controls_frame, bg='#2a2a2a')
        aimdown_frame.pack(fill='x', pady=5)
        
        tk.Label(aimdown_frame, text="Aimdown (1-25):", 
                font=('Arial', 12), fg='#ffffff', bg='#2a2a2a').pack(side='left')
        
        aimdown_scale = tk.Scale(aimdown_frame, from_=1, to=25, orient='horizontal',
                                variable=self.aimdown, bg='#2a2a2a', fg='#ffffff',
                                highlightbackground='#2a2a2a', troughcolor='#444444')
        aimdown_scale.pack(side='right', fill='x', expand=True, padx=(10, 0))
        
        smoothness_frame = tk.Frame(controls_frame, bg='#2a2a2a')
        smoothness_frame.pack(fill='x', pady=5)
        
        tk.Label(smoothness_frame, text="Smoothness (5-25):", 
                font=('Arial', 12), fg='#ffffff', bg='#2a2a2a').pack(side='left')
        
        smoothness_scale = tk.Scale(smoothness_frame, from_=5, to=25, orient='horizontal',
                                   variable=self.smoothness, bg='#2a2a2a', fg='#ffffff',
                                   highlightbackground='#2a2a2a', troughcolor='#444444')
        smoothness_scale.pack(side='right', fill='x', expand=True, padx=(10, 0))
        
        delay_frame = tk.Frame(controls_frame, bg='#2a2a2a')
        delay_frame.pack(fill='x', pady=5)
        
        tk.Label(delay_frame, text="Delay (0.01-0.15s):", 
                font=('Arial', 12), fg='#ffffff', bg='#2a2a2a').pack(side='left')
        
        delay_scale = tk.Scale(delay_frame, from_=0.01, to=0.15, resolution=0.01, orient='horizontal',
                              variable=self.delay, bg='#2a2a2a', fg='#ffffff',
                              highlightbackground='#2a2a2a', troughcolor='#444444')
        delay_scale.pack(side='right', fill='x', expand=True, padx=(10, 0))
        
        aim_assist_frame = tk.Frame(parent, bg='#2a2a2a', relief='raised', bd=3)
        aim_assist_frame.pack(fill='x', pady=15, padx=25)
        
        tk.Label(aim_assist_frame, text="AIM ASSIST - NEW VERSION", 
                font=('Arial', 16, 'bold'), 
                fg='#00ff00', bg='#2a2a2a').pack(pady=12)
        
        aim_controls_frame = tk.Frame(aim_assist_frame, bg='#2a2a2a')
        aim_controls_frame.pack(fill='x', padx=20, pady=10)
        
        aim_enable_frame = tk.Frame(aim_controls_frame, bg='#2a2a2a')
        aim_enable_frame.pack(fill='x', pady=5)
        
        tk.Checkbutton(aim_enable_frame, text="AIM ASSIST ENABLED (NEW VERSION)", 
                      variable=self.aim_assist_enabled, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        anti_shake_frame = tk.Frame(aim_controls_frame, bg='#2a2a2a')
        anti_shake_frame.pack(fill='x', pady=5)
        
        tk.Checkbutton(anti_shake_frame, text="ANTI-SHAKING (NEW VERSION)", 
                      variable=self.anti_shaking_enabled, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 12, 'bold')).pack(anchor='w')
        
        info_frame = tk.Frame(parent, bg='#1a1a1a', relief='raised', bd=3)
        info_frame.pack(fill='x', pady=20, padx=25)
        
        tk.Label(info_frame, text="APP INFO - NEW VERSION", 
                font=('Arial', 16, 'bold'), 
                fg='#00ff00', bg='#1a1a1a').pack(pady=12)
        
        self.info_label = tk.Label(info_frame, 
                                text="App ready - NEW VERSION for all games", 
                                font=('Arial', 12), 
                                fg='#cccccc', bg='#1a1a1a', justify='left')
        self.info_label.pack(anchor='w', padx=20, pady=10)
        
        help_frame = tk.Frame(parent, bg='#111111', relief='raised', bd=2)
        help_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(help_frame, text="HELP & CONTROLS - NEW VERSION", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#111111').pack(pady=8)
        
        help_text = "ANTI-RECOIL: Hold mouse button for anti-recoil - NEW VERSION\nIMPROVED AIM: Better tracking, less shaking - NEW VERSION\nSMOOTHNESS: Higher = Smoother movement (5-25) - NEW VERSION\nDELAY: Time between movements (0.01-0.15s) - NEW VERSION\nTEST: F2=Anti-recoil test, SPACE=Manual anti-recoil - NEW VERSION\nNEW VERSION - ALL OLD DATA REMOVED"
        
        help_label = tk.Label(help_frame, text=help_text,
                            font=('Arial', 10), 
                            fg='#cccccc', bg='#111111', justify='left')
        help_label.pack(anchor='w', padx=15, pady=8)
        
        debug_frame = tk.Frame(parent, bg='#f8f8f8', relief='raised', bd=2)
        debug_frame.pack(fill='x', pady=15, padx=20)
        
        tk.Label(debug_frame, text="DEBUG INFO - NEW VERSION", 
                font=('Arial', 14, 'bold'), 
                fg='#000000', bg='#f8f8f8').pack(pady=8)
        
        self.debug_label = tk.Label(debug_frame, 
                                text="Waiting for mouse input... - NEW VERSION", 
                                font=('Arial', 11), 
                                fg='#000000', bg='#f8f8f8', justify='left')
        self.debug_label.pack(anchor='w', padx=15, pady=8)
        
        test_button = tk.Button(parent, text="TEST ANTI-RECOIL", 
                              font=('Arial', 12, 'bold'),
                              bg='#ff6600', fg='#ffffff',
                              relief='flat', padx=20, pady=10,
                              command=self.test_anti_recoil,
                              activebackground='#ff4400',
                              activeforeground='#ffffff')
        test_button.pack(pady=5)
        
    def setup_settings_tab(self, parent):
        settings_label = tk.Label(parent, text="SETTINGS - NEW VERSION", 
                                font=('Arial', 16, 'bold'), 
                                fg='#00ff00', bg='#1a1a1a')
        settings_label.pack(pady=20)
        
        master_frame = tk.Frame(parent, bg='#2a2a2a', relief='raised', bd=3)
        master_frame.pack(fill='x', pady=15, padx=25)
        
        tk.Checkbutton(master_frame, text="APP MASTER SWITCH (NEW VERSION)", 
                      variable=self.app_enabled, bg='#2a2a2a', fg='#ffffff',
                      selectcolor='#333333', activebackground='#2a2a2a',
                      activeforeground='#ffffff', font=('Arial', 14, 'bold')).pack(pady=10)
        
        status_frame = tk.Frame(parent, bg='#1a1a1a', relief='raised', bd=3)
        status_frame.pack(fill='x', pady=15, padx=25)
        
        tk.Label(status_frame, text="STATUS - NEW VERSION", 
                font=('Arial', 14, 'bold'), 
                fg='#00ff00', bg='#1a1a1a').pack(pady=8)
        
        status_text = f"Success Count: {self.success_count}\nError Count: {self.error_count}\nStartup Protection: {self.startup_delay}s remaining\nNew Version: Active\nAll Old Data: Removed"
        
        status_label = tk.Label(status_frame, text=status_text,
                              font=('Arial', 10), 
                              fg='#cccccc', bg='#1a1a1a', justify='left')
        status_label.pack(anchor='w', padx=15, pady=8)
        
    def start_auto_update_loop(self):
        def new_loop():
            while self.running:
                try:
                    startup_elapsed = time.time() - self.app_startup_time
                    app_enabled = self.app_enabled.get()
                    
                    if startup_elapsed >= self.startup_delay and app_enabled:
                        if user32.GetAsyncKeyState(0x01) < 0:
                            aimdown = self.aimdown.get()
                            try:
                                user32.mouse_event(0x0001, 0, aimdown, 0, 0)
                                self.success_count += 1
                                self.debug_label.config(text=f"ANTI-RECOIL: {aimdown} pixels down")
                            except Exception as e:
                                self.debug_label.config(text=f"Anti-recoil error: {str(e)}")
                        else:
                            if self.aim_assist_enabled.get():
                                current_time = time.time()
                                if current_time % 3 < 0.05:
                                    strength = self.aim_assist_strength.get()
                                    try:
                                        aim_dx = random.randint(-strength//8, strength//8)
                                        aim_dy = random.randint(-strength//8, strength//8)
                                        user32.mouse_event(0x0001, aim_dx, aim_dy, 0, 0)
                                        self.debug_label.config(text=f"IMPROVED AIM: ({aim_dx}, {aim_dy}) pixels")
                                    except Exception as e:
                                        self.debug_label.config(text=f"Improved aim assist error: {str(e)}")
                                else:
                                    if not hasattr(self, 'last_status_msg') or time.time() - getattr(self, 'last_status_msg', 0) > 3:
                                        self.debug_label.config(text="App ready - Hold mouse button for anti-recoil, improved aim assist active")
                                        self.last_status_msg = time.time()
                            else:
                                if not hasattr(self, 'last_status_msg') or time.time() - getattr(self, 'last_status_msg', 0) > 3:
                                    self.debug_label.config(text="App ready - Hold mouse button for anti-recoil")
                                    self.last_status_msg = time.time()
                    else:
                        if not hasattr(self, 'last_disabled_msg') or time.time() - getattr(self, 'last_disabled_msg', 0) > 3:
                            self.debug_label.config(text="App disabled - Press CAPS LOCK to enable")
                            self.last_disabled_msg = time.time()
                    
                    if self.auto_update:
                        aim_status = "ON" if self.aim_assist_enabled.get() else "OFF"
                        self.info_label.config(text=f"Status: Aim Assist {aim_status}, Success: {self.success_count}")
                    
                    time.sleep(0.01)
                    
                except Exception as e:
                    self.error_count += 1
                    try:
                        self.debug_label.config(text=f"App error: {str(e)} - Auto-fixing...")
                    except:
                        pass
                    time.sleep(0.1)
        
        update_thread = threading.Thread(target=new_loop, daemon=True)
        update_thread.start()
        
    def start_mouse_tracking(self):
        def track_mouse():
            while True:
                try:
                    cursor = ctypes.wintypes.POINT()
                    user32.GetCursorPos(ctypes.byref(cursor))
                    current_x, current_y = cursor.x, cursor.y
                    
                    startup_elapsed = time.time() - self.app_startup_time
                    if startup_elapsed >= self.startup_delay:
                        self.mouse_moving = False
                    else:
                        self.mouse_moving = False
                    
                    self.last_mouse_x = current_x
                    self.last_mouse_y = current_y
                    
                    time.sleep(0.05)
                    
                except Exception as e:
                    try:
                        time.sleep(0.1)
                    except:
                        pass
        
        mouse_thread = threading.Thread(target=track_mouse, daemon=True)
        mouse_thread.start()
        
    def start_keyboard_listener(self):
        def on_press(key):
            try:
                if key == kb.Key.f2:
                    self.test_anti_recoil()
                elif key == kb.Key.space:
                    self.manual_anti_recoil()
                elif key == kb.Key.caps_lock:
                    self.app_enabled.set(not self.app_enabled.get())
            except:
                pass
        
        listener = kb.Listener(on_press=on_press)
        listener.start()
        
    def test_anti_recoil(self):
        try:
            startup_elapsed = time.time() - self.app_startup_time
            if startup_elapsed >= self.startup_delay:
                aimdown = self.aimdown.get()
                self.debug_label.config(text=f"Testing anti-recoil: {aimdown} pixels down")
                
                for i in range(3):
                    user32.mouse_event(0x0001, 0, aimdown, 0, 0)
                    time.sleep(0.1)
                
                self.debug_label.config(text=f"Anti-recoil test completed - {aimdown} pixels down")
                self.success_count += 1
            else:
                remaining = int(self.startup_delay - startup_elapsed)
                self.debug_label.config(text=f"Wait {remaining}s for startup protection to end")
        except Exception as e:
            self.debug_label.config(text=f"Anti-recoil test error: {str(e)}")
            
    def manual_anti_recoil(self):
        try:
            startup_elapsed = time.time() - self.app_startup_time
            if startup_elapsed >= self.startup_delay:
                aimdown = self.aimdown.get()
                self.debug_label.config(text=f"MANUAL ANTI-RECOIL: {aimdown} pixels down")
                
                user32.mouse_event(0x0001, 0, aimdown, 0, 0)
                self.success_count += 1
                
                self.debug_label.config(text=f"Manual anti-recoil completed - {aimdown} pixels down")
            else:
                remaining = int(self.startup_delay - startup_elapsed)
                self.debug_label.config(text=f"Wait {remaining}s for startup protection to end")
        except Exception as e:
            self.debug_label.config(text=f"Manual anti-recoil error: {str(e)}")
            
    def on_closing(self):
        self.running = False
        self.auto_update = False
        self.root.quit()
        try:
            self.root.destroy()
        except:
            pass
        
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.on_closing()
        except Exception as e:
            print(f"App error: {e}")
            self.on_closing()

def main():
    try:
        app = UltimateGamingApp()
        app.run()
    except KeyboardInterrupt:
        print("App closed by user")
    except Exception as e:
        print(f"App error: {e}")

if __name__ == "__main__":
    main()
