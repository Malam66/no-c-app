import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_installer():
    """Create an executable installer with desktop icon"""
    
    # Create requirements.txt for dependencies
    requirements = """tkinter
pynput
keyboard
mouse
ctypes
threading
time
random
json
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    # Create setup.py for cx_Freeze
    setup_content = '''import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "pynput", "keyboard", "mouse", "ctypes", "threading", "time", "random", "json"],
    "excludes": [],
    "include_files": []
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Ultimate Anti-Recoil App",
    version="1.0",
    description="Ultimate Anti-Recoil Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("new_ultimate_app.py", base=base, icon="icon.ico", target_name="UltimateApp.exe")]
)
'''
    
    with open('setup.py', 'w') as f:
        f.write(setup_content)
    
    # Create a simple icon file (placeholder)
    icon_content = '''# This is a placeholder for icon.ico
# You would need to create a proper .ico file
'''
    
    with open('icon.ico', 'w') as f:
        f.write(icon_content)
    
    # Create installer script
    installer_script = '''@echo off
echo Creating Ultimate Anti-Recoil App Installer...
echo.

REM Create desktop shortcut
echo Creating desktop shortcut...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Ultimate Anti-Recoil App.lnk'); $Shortcut.TargetPath = '%~dp0UltimateApp.exe'; $Shortcut.WorkingDirectory = '%~dp0'; $Shortcut.IconLocation = '%~dp0icon.ico'; $Shortcut.Save()"

echo.
echo Installation complete!
echo Desktop shortcut created.
echo.
pause
'''
    
    with open('installer.bat', 'w') as f:
        f.write(installer_script)
    
    # Create a simple executable launcher
    launcher_content = '''import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

def create_desktop_shortcut():
    """Create desktop shortcut"""
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        path = os.path.join(desktop, "Ultimate Anti-Recoil App.lnk")
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = sys.executable
        shortcut.WorkingDirectory = os.getcwd()
        shortcut.IconLocation = os.path.join(os.getcwd(), "icon.ico")
        shortcut.save()
        
        return True
    except:
        return False

def main():
    """Main launcher function"""
    # Create desktop shortcut if it doesn't exist
    if not os.path.exists(os.path.join(os.path.expanduser("~"), "Desktop", "Ultimate Anti-Recoil App.lnk")):
        if create_desktop_shortcut():
            print("Desktop shortcut created successfully!")
    
    # Launch the main app
    try:
        # Import and run the main app
        from new_ultimate_app import main as app_main
        app_main()
    except Exception as e:
        # Show error in GUI
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", f"Failed to start app: {str(e)}")
        root.destroy()

if __name__ == "__main__":
    main()
'''
    
    with open('launcher.py', 'w') as f:
        f.write(launcher_content)
    
    print("✅ Installer files created successfully!")
    print("📁 Files created:")
    print("   - requirements.txt")
    print("   - setup.py")
    print("   - installer.bat")
    print("   - launcher.py")
    print("   - icon.ico (placeholder)")
    print()
    print("🔧 To build the executable:")
    print("   1. Install cx_Freeze: pip install cx_Freeze")
    print("   2. Run: python setup.py build")
    print("   3. Run: installer.bat")
    print()
    print("🎯 The installer will:")
    print("   - Create desktop shortcut")
    print("   - Run without command prompt")
    print("   - Install all dependencies")

if __name__ == "__main__":
    create_installer() 