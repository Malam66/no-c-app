#!/usr/bin/env python3
"""
Remove Old App and Install New App on Web
Removes all old versions and installs only the latest app
"""

import os
import shutil
import subprocess
import sys

def remove_old_apps():
    """Remove all old app versions"""
    print("🗑️ Removing old app versions...")
    
    # List of old app files to remove
    old_files = [
        "ultimate_app_final.py",
        "ultimate_app_simple.py",
        "ultimate_auto_script.py",
        "enhanced_app.py",
        "no_shake_app.py",
        "new_ultimate_app.py.bak",
        "app_old.py",
        "app_backup.py"
    ]
    
    # List of old directories to remove
    old_dirs = [
        "old_app",
        "backup",
        "old_version",
        "previous_version"
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
    
    print("✅ All old app versions removed!")

def create_new_web_app():
    """Create new web app with only latest version"""
    print("🌐 Creating new web app with latest version...")
    
    # Create new web directory
    web_dir = "new_web_app"
    if os.path.exists(web_dir):
        shutil.rmtree(web_dir)
    os.makedirs(web_dir)
    
    # Copy ONLY the latest app
    shutil.copy("new_ultimate_app.py", os.path.join(web_dir, "ultimate_gaming_app.py"))
    
    # Create requirements.txt
    with open(os.path.join(web_dir, "requirements.txt"), "w") as f:
        f.write("""flask==2.3.3
gunicorn==21.2.0
tkinter
pynput
keyboard
mouse
pillow
""")
    
    # Create web app with only new app
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
        # Start ONLY the new app
        subprocess.Popen([sys.executable, 'ultimate_gaming_app.py'])
        return jsonify({"status": "success", "message": "NEW APP started successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download')
def download_app():
    try:
        # Send ONLY the new app file
        return send_file('ultimate_gaming_app.py', 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app.py',
                        mimetype='text/plain')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download_package')
def download_package():
    try:
        # Create a zip package with ONLY new app
        import zipfile
        zip_filename = 'ultimate_gaming_app_new.zip'
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Add ONLY new app
            zipf.write('ultimate_gaming_app.py', 'ultimate_gaming_app.py')
            # Add requirements
            zipf.write('requirements.txt', 'requirements.txt')
            # Add README
            zipf.write('README_NEW.md', 'README.md')
            # Add installer
            zipf.write('install_new.bat', 'install.bat')
        
        return send_file(zip_filename, 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app_new.zip',
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
    
    # Create HTML template for NEW APP ONLY
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Gaming App - NEW VERSION ONLY</title>
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
        .new-badge {
            background: #ff6600;
            color: white;
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
        .new-info {
            background: rgba(255,255,0,0.1);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #ffff00;
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
        <h1>🎯 Ultimate Gaming App<span class="new-badge">NEW VERSION ONLY</span></h1>
        
        <div class="new-info">
            <h3>🔥 NEW VERSION INSTALLED - OLD VERSIONS REMOVED</h3>
            <p><strong>This is the ONLY version available - All old versions have been removed!</strong></p>
            <ul>
                <li>✅ NEW Anti-recoil: Works perfectly in all games</li>
                <li>✅ NEW Improved aim assist: Better tracking, less shaking</li>
                <li>✅ NEW Mouse control protection: Full user control priority</li>
                <li>✅ NEW Startup protection: 10-second delay prevents issues</li>
                <li>✅ NEW Error handling: Automatic error recovery</li>
            </ul>
        </div>
        
        <div class="removed-info">
            <h3>🗑️ OLD VERSIONS REMOVED</h3>
            <p><strong>All old app versions have been completely removed from the system!</strong></p>
            <ul>
                <li>❌ Removed: ultimate_app_final.py</li>
                <li>❌ Removed: ultimate_app_simple.py</li>
                <li>❌ Removed: ultimate_auto_script.py</li>
                <li>❌ Removed: enhanced_app.py</li>
                <li>❌ Removed: no_shake_app.py</li>
                <li>❌ Removed: All backup files</li>
            </ul>
        </div>
        
        <div class="feature">
            <h3>🔫 NEW Anti-Recoil - LATEST VERSION</h3>
            <p>Hold mouse button for automatic recoil compensation - Works in ALL games</p>
        </div>
        
        <div class="feature">
            <h3>🎯 NEW Improved Aim Assist - LATEST VERSION</h3>
            <p>Better tracking with less shaking - Enhanced enemy detection</p>
        </div>
        
        <div class="feature">
            <h3>⚙️ NEW Features Only</h3>
            <ul>
                <li>NEW Anti-recoil system (LATEST VERSION)</li>
                <li>NEW Improved aim assist (LATEST VERSION)</li>
                <li>NEW Mouse control protection (LATEST VERSION)</li>
                <li>NEW Startup protection (LATEST VERSION)</li>
                <li>NEW Error handling (LATEST VERSION)</li>
            </ul>
        </div>
        
        <div style="text-align: center;">
            <button class="button" onclick="startNewApp()">🚀 Start NEW App</button>
            <button class="button download-button" onclick="downloadNewApp()">📥 Download NEW App</button>
            <button class="button download-button" onclick="downloadPackage()">📦 Download NEW Package</button>
        </div>
        
        <div id="status" class="status" style="display: none;">
            <p id="statusText">Ready to start NEW version...</p>
        </div>
        
        <div class="feature">
            <h3>🎮 NEW Controls - LATEST VERSION</h3>
            <ul>
                <li><strong>Hold Mouse Button:</strong> NEW Anti-recoil</li>
                <li><strong>Press SPACE:</strong> NEW Manual anti-recoil</li>
                <li><strong>Press F2:</strong> NEW Test anti-recoil</li>
                <li><strong>Press F5:</strong> NEW Test aim assist</li>
                <li><strong>CAPS LOCK:</strong> NEW Master switch</li>
            </ul>
        </div>
        
        <div class="feature">
            <h3>🛡️ NEW Safety Features - LATEST VERSION</h3>
            <ul>
                <li><strong>NEW Startup Protection:</strong> 10-second delay</li>
                <li><strong>NEW Mouse Control Priority:</strong> Your movements take priority</li>
                <li><strong>NEW Error Handling:</strong> Automatic recovery</li>
                <li><strong>NEW Graceful Shutdown:</strong> Clean app closing</li>
            </ul>
        </div>
    </div>
    
    <script>
        function startNewApp() {
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
        
        function downloadNewApp() {
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
    
    # Create new README
    new_readme = """# 🎯 ULTIMATE GAMING APP - NEW VERSION ONLY

## 🔥 NEW VERSION INSTALLED - OLD VERSIONS REMOVED

### ✅ NEW COMPLETE FIXES:
- **NEW Anti-recoil**: Works perfectly in all games
- **NEW Improved aim assist**: Better tracking, less shaking
- **NEW Mouse control protection**: Full user control priority
- **NEW Startup protection**: 10-second delay prevents issues
- **NEW Error handling**: Automatic error recovery

### 🗑️ OLD VERSIONS REMOVED:
- ❌ Removed: ultimate_app_final.py
- ❌ Removed: ultimate_app_simple.py
- ❌ Removed: ultimate_auto_script.py
- ❌ Removed: enhanced_app.py
- ❌ Removed: no_shake_app.py
- ❌ Removed: All backup files

### 🎮 NEW CONTROLS:
- **Hold Mouse Button**: NEW Anti-recoil
- **Press SPACE**: NEW Manual anti-recoil
- **Press F2**: NEW Test anti-recoil
- **Press F5**: NEW Test aim assist
- **CAPS LOCK**: NEW Master switch

### 🛡️ NEW SAFETY FEATURES:
- **NEW Startup Protection**: 10-second delay
- **NEW Mouse Control Priority**: Your movements take priority
- **NEW Error Handling**: Automatic recovery
- **NEW Graceful Shutdown**: Clean app closing

## 🚀 INSTALLATION:

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the NEW app:**
   ```
   python ultimate_gaming_app.py
   ```

3. **Or use NEW installer:**
   ```
   install_new.bat
   ```

## ⚙️ NEW SETTINGS:

- **Aimdown**: Recoil strength (1-25)
- **Smoothness**: Movement smoothness (5-25)
- **Delay**: Time between movements (0.01-0.15s)
- **Aim Assist Strength**: Aim assist power (1-50)

## 🎯 NEW FEATURES:

### NEW Anti-Recoil:
- Hold mouse button for automatic recoil compensation
- Adjustable strength settings
- Works with all games

### NEW Improved Aim Assist:
- Automatically detects enemy movement
- Provides precise aim assistance
- Reduced shaking for better control

## 📁 NEW FILES INCLUDED:

- `ultimate_gaming_app.py`: NEW app version only
- `requirements.txt`: Python dependencies
- `install_new.bat`: NEW Windows installer
- `app_icon.ico`: App icon
- `app_icon.png`: App icon

## ⚠️ DISCLAIMER:

This app is for educational and testing purposes. Use responsibly and in accordance with game terms of service.

---

**🎯 ULTIMATE GAMING APP - NEW VERSION ONLY - OLD VERSIONS REMOVED**
"""
    
    with open(os.path.join(web_dir, "README_NEW.md"), "w", encoding="utf-8") as f:
        f.write(new_readme)
    
    # Create new installer
    installer_content = """@echo off
echo ========================================
echo    ULTIMATE GAMING APP - NEW VERSION
echo ========================================
echo.
echo Installing NEW version...
echo OLD versions have been removed!
echo.
pip install -r requirements.txt
echo.
echo Installation complete!
echo.
echo To run the NEW app:
echo python ultimate_gaming_app.py
echo.
echo NEW Features:
echo - NEW Anti-recoil system
echo - NEW Improved aim assist
echo - NEW Mouse control protection
echo - NEW Startup protection
echo.
echo OLD versions have been removed!
echo.
pause
"""
    
    with open(os.path.join(web_dir, "install_new.bat"), "w") as f:
        f.write(installer_content)
    
    print("✅ New web app created with only latest version!")
    return web_dir

def deploy_new_to_github():
    """Deploy new version to GitHub"""
    print("📦 Deploying NEW version to GitHub...")
    
    try:
        # Force add all files
        subprocess.run(["git", "add", "-A"], check=True)
        print("✅ All files added to git")
        
        # Force commit with new message
        subprocess.run(["git", "commit", "-m", "🔥 NEW VERSION ONLY - OLD VERSIONS REMOVED"], check=True)
        print("✅ Changes committed")
        
        # Force push to GitHub
        subprocess.run(["git", "push", "--force", "origin", "main"], check=True)
        print("✅ Force pushed to GitHub successfully!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during deployment: {e}")
        return False

def main():
    """Main function"""
    print("🚀 Starting remove old and install new process...")
    
    # Remove old apps
    remove_old_apps()
    
    # Create new web app
    web_dir = create_new_web_app()
    
    # Deploy to GitHub
    success = deploy_new_to_github()
    
    if success:
        print("🎉 Process completed successfully!")
        print(f"📁 New web app created in: {web_dir}")
        print("🗑️ All old versions removed")
        print("🌐 GitHub updated with NEW version only")
        print("🌐 To run new web app: cd new_web_app && python web_app.py")
    else:
        print("❌ Process failed")
        print("💡 Please check your git configuration")

if __name__ == "__main__":
    main() 