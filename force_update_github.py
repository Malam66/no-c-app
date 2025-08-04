#!/usr/bin/env python3
"""
Force Update GitHub Script for Ultimate Gaming App
Forces update the GitHub repository with the latest app version
"""

import os
import shutil
import subprocess
import sys

def force_update_github():
    """Force update GitHub with latest app"""
    print("🚀 Force updating GitHub with latest app...")
    
    try:
        # Add all files including the latest app
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Files added to git")
        
        # Force commit with new message
        subprocess.run(["git", "commit", "-m", "🔥 ULTIMATE GAMING APP - LATEST VERSION - COMPLETE FIX"], check=True)
        print("✅ Changes committed")
        
        # Force push to GitHub
        subprocess.run(["git", "push", "--force", "origin", "main"], check=True)
        print("✅ Force pushed to GitHub successfully!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during force update: {e}")
        return False

def create_latest_release():
    """Create latest release package"""
    print("📦 Creating latest release package...")
    
    release_dir = "latest_release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # Copy latest app files
    files_to_copy = [
        "new_ultimate_app.py",
        "requirements.txt",
        "README.md",
        "app_icon.ico",
        "app_icon.png"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy(file, release_dir)
            print(f"✅ Copied {file}")
    
    # Create latest installer
    installer_content = """@echo off
echo ========================================
echo    ULTIMATE GAMING APP - LATEST VERSION
echo ========================================
echo.
echo Installing latest version...
pip install -r requirements.txt
echo.
echo Installation complete!
echo.
echo To run the app:
echo python new_ultimate_app.py
echo.
echo Features:
echo - Anti-recoil system
echo - Improved aim assist
echo - Mouse control protection
echo - Startup protection
echo.
pause
"""
    
    with open(os.path.join(release_dir, "install_latest.bat"), "w") as f:
        f.write(installer_content)
    
    # Create latest README
    latest_readme = """# 🎯 ULTIMATE GAMING APP - LATEST VERSION

## 🔥 NEW FEATURES (Latest Update)

### ✅ COMPLETE FIXES:
- **Anti-recoil**: Works perfectly in all games
- **Improved aim assist**: Better tracking, less shaking
- **Mouse control protection**: Full user control priority
- **Startup protection**: 10-second delay prevents issues
- **Error handling**: Automatic error recovery

### 🎮 CONTROLS:
- **Hold Mouse Button**: Anti-recoil
- **Press SPACE**: Manual anti-recoil
- **Press F2**: Test anti-recoil
- **Press F5**: Test aim assist
- **CAPS LOCK**: Master switch

### 🛡️ SAFETY FEATURES:
- **Startup Protection**: 10-second delay
- **Mouse Control Priority**: Your movements take priority
- **Error Handling**: Automatic recovery
- **Graceful Shutdown**: Clean app closing

## 🚀 INSTALLATION:

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```
   python new_ultimate_app.py
   ```

3. **Or use installer:**
   ```
   install_latest.bat
   ```

## ⚙️ SETTINGS:

- **Aimdown**: Recoil strength (1-25)
- **Smoothness**: Movement smoothness (5-25)
- **Delay**: Time between movements (0.01-0.15s)
- **Aim Assist Strength**: Aim assist power (1-50)

## 🎯 FEATURES:

### Anti-Recoil:
- Hold mouse button for automatic recoil compensation
- Adjustable strength settings
- Works with all games

### Improved Aim Assist:
- Automatically detects enemy movement
- Provides precise aim assistance
- Reduced shaking for better control

## 📁 FILES INCLUDED:

- `new_ultimate_app.py`: Latest app version
- `requirements.txt`: Python dependencies
- `install_latest.bat`: Windows installer
- `app_icon.ico`: App icon
- `app_icon.png`: App icon

## ⚠️ DISCLAIMER:

This app is for educational and testing purposes. Use responsibly and in accordance with game terms of service.

---

**🎯 ULTIMATE GAMING APP - LATEST VERSION - COMPLETE FIX**
"""
    
    with open(os.path.join(release_dir, "README_LATEST.md"), "w", encoding="utf-8") as f:
        f.write(latest_readme)
    
    print("✅ Latest release package created!")
    return release_dir

def main():
    """Main force update function"""
    print("🚀 Starting force update process...")
    
    # Create latest release
    release_dir = create_latest_release()
    
    # Force update GitHub
    success = force_update_github()
    
    if success:
        print("🎉 Force update completed successfully!")
        print(f"📁 Latest release created in: {release_dir}")
        print("🌐 GitHub repository updated with latest version")
        print("📦 Users will now download the latest version")
    else:
        print("❌ Force update failed")
        print("💡 Please check your git configuration")

if __name__ == "__main__":
    main() 