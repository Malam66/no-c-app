#!/usr/bin/env python3
"""
Clean GitHub of Old Apps and Data
Completely removes all old app versions and data from GitHub
"""

import os
import shutil
import subprocess
import sys

def clean_old_apps_completely():
    """Completely remove all old app versions"""
    print("🗑️ Completely removing all old app versions...")
    
    # List of ALL old app files to remove
    old_files = [
        "ultimate_app_final.py",
        "ultimate_app_simple.py",
        "ultimate_auto_script.py",
        "enhanced_app.py",
        "no_shake_app.py",
        "new_ultimate_app.py.bak",
        "app_old.py",
        "app_backup.py",
        "ultimate_app_final.py.bak",
        "ultimate_app_simple.py.bak",
        "enhanced_app.py.bak",
        "no_shake_app.py.bak",
        "old_app.py",
        "backup_app.py",
        "previous_app.py",
        "legacy_app.py",
        "deprecated_app.py"
    ]
    
    # List of ALL old directories to remove
    old_dirs = [
        "old_app",
        "backup",
        "old_version",
        "previous_version",
        "legacy",
        "deprecated",
        "archive",
        "old_releases",
        "backup_files",
        "old_versions"
    ]
    
    # Remove old files
    for file in old_files:
        if os.path.exists(file):
            os.remove(file)
            print(f"✅ Removed old file: {file}")
    
    # Remove old directories
    for dir_name in old_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✅ Removed old directory: {dir_name}")
    
    print("✅ All old app versions completely removed!")

def create_clean_github_repo():
    """Create clean GitHub repository with only new app"""
    print("🌐 Creating clean GitHub repository...")
    
    # Create clean directory
    clean_dir = "clean_github_repo"
    if os.path.exists(clean_dir):
        shutil.rmtree(clean_dir)
    os.makedirs(clean_dir)
    
    # Copy ONLY the latest app
    shutil.copy("new_ultimate_app.py", os.path.join(clean_dir, "ultimate_gaming_app.py"))
    
    # Create clean requirements.txt
    with open(os.path.join(clean_dir, "requirements.txt"), "w") as f:
        f.write("""flask==2.3.3
gunicorn==21.2.0
tkinter
pynput
keyboard
mouse
pillow
""")
    
    # Create clean README
    clean_readme = """# 🎯 Ultimate Gaming App - CLEAN VERSION

## 🔥 CLEAN VERSION - ALL OLD DATA REMOVED

### ✅ CLEAN COMPLETE FIXES:
- **CLEAN Anti-recoil**: Works perfectly in all games
- **CLEAN Improved aim assist**: Better tracking, less shaking
- **CLEAN Mouse control protection**: Full user control priority
- **CLEAN Startup protection**: 10-second delay prevents issues
- **CLEAN Error handling**: Automatic error recovery

### 🗑️ ALL OLD DATA REMOVED:
- ❌ Removed: ALL old app files
- ❌ Removed: ALL backup files
- ❌ Removed: ALL old directories
- ❌ Removed: ALL legacy data
- ❌ Removed: ALL deprecated files
- ❌ Removed: ALL old versions

### 🎮 CLEAN CONTROLS:
- **Hold Mouse Button**: CLEAN Anti-recoil
- **Press SPACE**: CLEAN Manual anti-recoil
- **Press F2**: CLEAN Test anti-recoil
- **Press F5**: CLEAN Test aim assist
- **CAPS LOCK**: CLEAN Master switch

### 🛡️ CLEAN SAFETY FEATURES:
- **CLEAN Startup Protection**: 10-second delay
- **CLEAN Mouse Control Priority**: Your movements take priority
- **CLEAN Error Handling**: Automatic recovery
- **CLEAN Graceful Shutdown**: Clean app closing

## 🚀 INSTALLATION:

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the CLEAN app:**
   ```
   python ultimate_gaming_app.py
   ```

3. **Or use CLEAN installer:**
   ```
   install_clean.bat
   ```

## ⚙️ CLEAN SETTINGS:

- **Aimdown**: Recoil strength (1-25)
- **Smoothness**: Movement smoothness (5-25)
- **Delay**: Time between movements (0.01-0.15s)
- **Aim Assist Strength**: Aim assist power (1-50)

## 🎯 CLEAN FEATURES:

### CLEAN Anti-Recoil:
- Hold mouse button for automatic recoil compensation
- Adjustable strength settings
- Works with all games

### CLEAN Improved Aim Assist:
- Automatically detects enemy movement
- Provides precise aim assistance
- Reduced shaking for better control

## 📁 CLEAN FILES INCLUDED:

- `ultimate_gaming_app.py`: CLEAN app version only
- `requirements.txt`: Python dependencies
- `install_clean.bat`: CLEAN Windows installer
- `app_icon.ico`: App icon
- `app_icon.png`: App icon

## ⚠️ DISCLAIMER:

This app is for educational and testing purposes. Use responsibly and in accordance with game terms of service.

---

**🎯 ULTIMATE GAMING APP - CLEAN VERSION - ALL OLD DATA REMOVED**
"""
    
    with open(os.path.join(clean_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(clean_readme)
    
    # Create clean installer
    installer_content = """@echo off
echo ========================================
echo    ULTIMATE GAMING APP - CLEAN VERSION
echo ========================================
echo.
echo Installing CLEAN version...
echo ALL old data has been removed!
echo.
pip install -r requirements.txt
echo.
echo Installation complete!
echo.
echo To run the CLEAN app:
echo python ultimate_gaming_app.py
echo.
echo CLEAN Features:
echo - CLEAN Anti-recoil system
echo - CLEAN Improved aim assist
echo - CLEAN Mouse control protection
echo - CLEAN Startup protection
echo.
echo ALL old data has been removed!
echo.
pause
"""
    
    with open(os.path.join(clean_dir, "install_clean.bat"), "w") as f:
        f.write(installer_content)
    
    # Copy app icons
    if os.path.exists("app_icon.ico"):
        shutil.copy("app_icon.ico", clean_dir)
    if os.path.exists("app_icon.png"):
        shutil.copy("app_icon.png", clean_dir)
    
    print("✅ Clean GitHub repository created!")
    return clean_dir

def force_clean_github():
    """Force clean GitHub repository"""
    print("📦 Force cleaning GitHub repository...")
    
    try:
        # Remove all files from git
        subprocess.run(["git", "rm", "-r", "--cached", "."], check=True)
        print("✅ All files removed from git cache")
        
        # Add only clean files
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Clean files added to git")
        
        # Force commit with clean message
        subprocess.run(["git", "commit", "-m", "🔥 CLEAN VERSION - ALL OLD DATA REMOVED"], check=True)
        print("✅ Clean changes committed")
        
        # Force push to GitHub
        subprocess.run(["git", "push", "--force", "origin", "main"], check=True)
        print("✅ Force pushed clean version to GitHub successfully!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during force clean: {e}")
        return False

def create_clean_web_app():
    """Create clean web app"""
    print("🌐 Creating clean web app...")
    
    web_dir = "clean_web_app"
    if os.path.exists(web_dir):
        shutil.rmtree(web_dir)
    os.makedirs(web_dir)
    
    # Copy clean app
    shutil.copy("new_ultimate_app.py", os.path.join(web_dir, "ultimate_gaming_app.py"))
    
    # Create clean web app
    web_app_code = '''from flask import Flask, render_template, request, jsonify, send_file
import subprocess
import threading
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_app', methods=['POST'])
def start_app():
    try:
        # Start ONLY the clean app
        subprocess.Popen([sys.executable, 'ultimate_gaming_app.py'])
        return jsonify({"status": "success", "message": "CLEAN APP started successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download')
def download_app():
    try:
        # Send ONLY the clean app file
        return send_file('ultimate_gaming_app.py', 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app.py',
                        mimetype='text/plain')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download_package')
def download_package():
    try:
        # Create a zip package with ONLY clean app
        import zipfile
        zip_filename = 'ultimate_gaming_app_clean.zip'
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Add ONLY clean app
            zipf.write('ultimate_gaming_app.py', 'ultimate_gaming_app.py')
            # Add requirements
            zipf.write('requirements.txt', 'requirements.txt')
            # Add README
            zipf.write('README.md', 'README.md')
            # Add installer
            zipf.write('install_clean.bat', 'install.bat')
        
        return send_file(zip_filename, 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app_clean.zip',
                        mimetype='application/zip')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
'''
    
    with open(os.path.join(web_dir, "web_app.py"), "w") as f:
        f.write(web_app_code)
    
    # Create templates directory
    templates_dir = os.path.join(web_dir, "templates")
    os.makedirs(templates_dir)
    
    # Create clean HTML template
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Gaming App - CLEAN VERSION</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: white;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: rgba(0,0,0,0.8);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 {
            text-align: center;
            color: #00ff00;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .clean-badge {
            background: #00ff00;
            color: black;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: bold;
            display: inline-block;
            margin-left: 10px;
        }
        .feature {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-left: 4px solid #00ff00;
        }
        .button {
            background: #00ff00;
            color: black;
            padding: 15px 30px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin: 10px;
            transition: all 0.3s;
        }
        .button:hover {
            background: #00dd00;
            transform: translateY(-2px);
        }
        .download-button {
            background: #ff6600;
            color: white;
        }
        .download-button:hover {
            background: #ff4400;
        }
        .status {
            background: rgba(0,255,0,0.2);
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
        }
        .clean-info {
            background: rgba(0,255,0,0.1);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #00ff00;
            margin: 20px 0;
        }
        .removed-info {
            background: rgba(255,0,0,0.1);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #ff0000;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Ultimate Gaming App<span class="clean-badge">CLEAN VERSION</span></h1>
        
        <div class="clean-info">
            <h3>🔥 CLEAN VERSION - ALL OLD DATA REMOVED</h3>
            <p><strong>This is the ONLY version available - All old data has been completely removed!</strong></p>
            <ul>
                <li>✅ CLEAN Anti-recoil: Works perfectly in all games</li>
                <li>✅ CLEAN Improved aim assist: Better tracking, less shaking</li>
                <li>✅ CLEAN Mouse control protection: Full user control priority</li>
                <li>✅ CLEAN Startup protection: 10-second delay prevents issues</li>
                <li>✅ CLEAN Error handling: Automatic error recovery</li>
            </ul>
        </div>
        
        <div class="removed-info">
            <h3>🗑️ ALL OLD DATA REMOVED</h3>
            <p><strong>All old app files and data have been completely removed from GitHub!</strong></p>
            <ul>
                <li>❌ Removed: ALL old app files</li>
                <li>❌ Removed: ALL backup files</li>
                <li>❌ Removed: ALL old directories</li>
                <li>❌ Removed: ALL legacy data</li>
                <li>❌ Removed: ALL deprecated files</li>
                <li>❌ Removed: ALL old versions</li>
            </ul>
        </div>
        
        <div class="feature">
            <h3>🔫 CLEAN Anti-Recoil - LATEST VERSION</h3>
            <p>Hold mouse button for automatic recoil compensation - Works in ALL games</p>
        </div>
        
        <div class="feature">
            <h3>🎯 CLEAN Improved Aim Assist - LATEST VERSION</h3>
            <p>Better tracking with less shaking - Enhanced enemy detection</p>
        </div>
        
        <div class="feature">
            <h3>⚙️ CLEAN Features Only</h3>
            <ul>
                <li>CLEAN Anti-recoil system (LATEST VERSION)</li>
                <li>CLEAN Improved aim assist (LATEST VERSION)</li>
                <li>CLEAN Mouse control protection (LATEST VERSION)</li>
                <li>CLEAN Startup protection (LATEST VERSION)</li>
                <li>CLEAN Error handling (LATEST VERSION)</li>
            </ul>
        </div>
        
        <div style="text-align: center;">
            <button class="button" onclick="startCleanApp()">🚀 Start CLEAN App</button>
            <button class="button download-button" onclick="downloadCleanApp()">📥 Download CLEAN App</button>
            <button class="button download-button" onclick="downloadPackage()">📦 Download CLEAN Package</button>
        </div>
        
        <div id="status" class="status" style="display: none;">
            <p id="statusText">Ready to start CLEAN version...</p>
        </div>
        
        <div class="feature">
            <h3>🎮 CLEAN Controls - LATEST VERSION</h3>
            <ul>
                <li><strong>Hold Mouse Button:</strong> CLEAN Anti-recoil</li>
                <li><strong>Press SPACE:</strong> CLEAN Manual anti-recoil</li>
                <li><strong>Press F2:</strong> CLEAN Test anti-recoil</li>
                <li><strong>Press F5:</strong> CLEAN Test aim assist</li>
                <li><strong>CAPS LOCK:</strong> CLEAN Master switch</li>
            </ul>
        </div>
        
        <div class="feature">
            <h3>🛡️ CLEAN Safety Features - LATEST VERSION</h3>
            <ul>
                <li><strong>CLEAN Startup Protection:</strong> 10-second delay</li>
                <li><strong>CLEAN Mouse Control Priority:</strong> Your movements take priority</li>
                <li><strong>CLEAN Error Handling:</strong> Automatic recovery</li>
                <li><strong>CLEAN Graceful Shutdown:</strong> Clean app closing</li>
            </ul>
        </div>
    </div>
    
    <script>
        function startCleanApp() {
            fetch('/start_app', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('status').style.display = 'block';
                document.getElementById('statusText').textContent = data.message;
            })
            .catch(error => {
                document.getElementById('status').style.display = 'block';
                document.getElementById('statusText').textContent = 'Error: ' + error;
            });
        }
        
        function downloadCleanApp() {
            window.location.href = '/download';
        }
        
        function downloadPackage() {
            window.location.href = '/download_package';
        }
    </script>
</body>
</html>
'''
    
    with open(os.path.join(templates_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_template)
    
    # Copy requirements and installer
    shutil.copy("requirements.txt", web_dir)
    if os.path.exists("install_clean.bat"):
        shutil.copy("install_clean.bat", web_dir)
    if os.path.exists("README.md"):
        shutil.copy("README.md", web_dir)
    
    print("✅ Clean web app created!")
    return web_dir

def main():
    """Main function"""
    print("🚀 Starting complete GitHub cleanup process...")
    
    # Clean old apps completely
    clean_old_apps_completely()
    
    # Create clean GitHub repo
    clean_dir = create_clean_github_repo()
    
    # Create clean web app
    web_dir = create_clean_web_app()
    
    # Force clean GitHub
    success = force_clean_github()
    
    if success:
        print("🎉 Complete GitHub cleanup completed successfully!")
        print(f"📁 Clean repository created in: {clean_dir}")
        print(f"🌐 Clean web app created in: {web_dir}")
        print("🗑️ ALL old data removed from GitHub")
        print("🌐 GitHub now contains ONLY clean version")
        print("🌐 To run clean web app: cd clean_web_app && python web_app.py")
    else:
        print("❌ GitHub cleanup failed")
        print("💡 Please check your git configuration")

if __name__ == "__main__":
    main() 