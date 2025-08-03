import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "pynput", "keyboard", "mouse", "ctypes", "threading", "time", "random", "math"],
    "excludes": [],
    "include_files": []
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # This prevents CMD window from showing

setup(
    name="Ultimate Anti-Recoil App",
    version="2.0.0",
    description="Ultimate Anti-Recoil Application with Aim Assist",
    options={"build_exe": build_exe_options},
    executables=[Executable("new_ultimate_app.py", base=base, target_name="UltimateAntiRecoilApp.exe", icon="app_icon.ico")]
)
