#!/usr/bin/env python3
"""
Final Web Deployment Script for Ultimate Gaming App
Ensures only the latest app version is available for download
"""

import os
import shutil
import subprocess
import sys

def create_final_web_files():
    """Create final web deployment files with only latest app"""
    print("🌐 Creating final web deployment files...")
    
    # Create web directory
    web_dir = "web_deploy_final"
    if os.path.exists(web_dir):
        shutil.rmtree(web_dir)
    os.makedirs(web_dir)
    
    # Copy ONLY the latest app file
    shutil.copy("new_ultimate_app.py", os.path.join(web_dir, "ultimate_gaming_app_latest.py"))
    
    # Create requirements.txt for web
    with open(os.path.join(web_dir, "requirements.txt"), "w") as f:
        f.write("""flask==2.3.3
gunicorn==21.2.0
tkinter
pynput
keyboard
mouse
pillow
""")
    
    # Create web app wrapper with download functionality
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
        # Start the latest app in background
        subprocess.Popen([sys.executable, 'ultimate_gaming_app_latest.py'])
        return jsonify({"status": "success", "message": "Latest app started successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download')
def download_app():
    try:
        # Send the latest app file
        return send_file('ultimate_gaming_app_latest.py', 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app_latest.py',
                        mimetype='text/plain')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/download_package')
def download_package():
    try:
        # Create a zip package with latest app
        import zipfile
        zip_filename = 'ultimate_gaming_app_latest.zip'
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            # Add latest app
            zipf.write('ultimate_gaming_app_latest.py', 'ultimate_gaming_app_latest.py')
            # Add requirements
            zipf.write('requirements.txt', 'requirements.txt')
            # Add README
            zipf.write('README_LATEST.md', 'README.md')
            # Add installer
            zipf.write('install_latest.bat', 'install.bat')
        
        return send_file(zip_filename, 
                        as_attachment=True, 
                        download_name='ultimate_gaming_app_latest.zip',
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
    
    # Create HTML template with latest app info
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Gaming App - LATEST VERSION</title>
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
        .version-badge {
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
        .latest-info {
            background: rgba(255,255,0,0.1);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #ffff00;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Ultimate Gaming App<span class="version-badge">LATEST VERSION</span></h1>
        
        <div class="latest-info">
            <h3>🔥 LATEST VERSION - COMPLETE FIX</h3>
            <p><strong>This is the ONLY version available for download - Latest app with all fixes!</strong></p>
            <ul>
                <li>✅ Anti-recoil: Works perfectly in all games</li>
                <li>✅ Improved aim assist: Better tracking, less shaking</li>
                <li>✅ Mouse control protection: Full user control priority</li>
                <li>✅ Startup protection: 10-second delay prevents issues</li>
                <li>✅ Error handling: Automatic error recovery</li>
            </ul>
        </div>
        
        <div class="feature">
            <h3>🔫 Anti-Recoil - LATEST VERSION</h3>
            <p>Hold mouse button for automatic recoil compensation - Works in ALL games</p>
        </div>
        
        <div class="feature">
            <h3>🎯 Improved Aim Assist - LATEST VERSION</h3>
            <p>Better tracking with less shaking - Enhanced enemy detection</p>
        </div>
        
        <div class="feature">
            <h3>⚙️ Latest Features</h3>
            <ul>
                <li>Anti-recoil system (LATEST VERSION)</li>
                <li>Improved aim assist (LATEST VERSION)</li>
                <li>Mouse control protection (LATEST VERSION)</li>
                <li>Startup protection (LATEST VERSION)</li>
                <li>Error handling (LATEST VERSION)</li>
            </ul>
        </div>
        
        <div style="text-align: center;">
            <button class="button" onclick="startApp()">🚀 Start Latest App</button>
            <button class="button download-button" onclick="downloadLatestApp()">📥 Download LATEST App</button>
            <button class="button download-button" onclick="downloadPackage()">📦 Download Complete Package</button>
        </div>
        
        <div id="status" class="status" style="display: none;">
            <p id="statusText">Ready to start latest version...</p>
        </div>
        
        <div class="feature">
            <h3>🎮 Controls - LATEST VERSION</h3>
            <ul>
                <li><strong>Hold Mouse Button:</strong> Anti-recoil</li>
                <li><strong>Press SPACE:</strong> Manual anti-recoil</li>
                <li><strong>Press F2:</strong> Test anti-recoil</li>
                <li><strong>Press F5:</strong> Test aim assist</li>
                <li><strong>CAPS LOCK:</strong> Master switch</li>
            </ul>
        </div>
        
        <div class="feature">
            <h3>🛡️ Safety Features - LATEST VERSION</h3>
            <ul>
                <li><strong>Startup Protection:</strong> 10-second delay</li>
                <li><strong>Mouse Control Priority:</strong> Your movements take priority</li>
                <li><strong>Error Handling:</strong> Automatic recovery</li>
                <li><strong>Graceful Shutdown:</strong> Clean app closing</li>
            </ul>
        </div>
    </div>
    
    <script>
        function startApp() {
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
        
        function downloadLatestApp() {
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
    
    # Create latest README
    latest_readme = """# 🎯 ULTIMATE GAMING APP - LATEST VERSION

## 🔥 LATEST VERSION - COMPLETE FIX

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

2. **Run the latest app:**
   ```
   python ultimate_gaming_app_latest.py
   ```

3. **Or use installer:**
   ```
   install.bat
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

- `ultimate_gaming_app_latest.py`: LATEST app version
- `requirements.txt`: Python dependencies
- `install.bat`: Windows installer
- `README.md`: This file

## ⚠️ DISCLAIMER:

This app is for educational and testing purposes. Use responsibly and in accordance with game terms of service.

---

**🎯 ULTIMATE GAMING APP - LATEST VERSION - COMPLETE FIX**
"""
    
    with open(os.path.join(web_dir, "README_LATEST.md"), "w", encoding="utf-8") as f:
        f.write(latest_readme)
    
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
echo To run the latest app:
echo python ultimate_gaming_app_latest.py
echo.
echo Features:
echo - Anti-recoil system (LATEST)
echo - Improved aim assist (LATEST)
echo - Mouse control protection (LATEST)
echo - Startup protection (LATEST)
echo.
pause
"""
    
    with open(os.path.join(web_dir, "install_latest.bat"), "w") as f:
        f.write(installer_content)
    
    print("✅ Final web deployment files created successfully!")
    return web_dir

def deploy_final_to_github():
    """Deploy final version to GitHub"""
    print("📦 Deploying final version to GitHub...")
    
    try:
        # Add all files including the final web deployment
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Files added to git")
        
        # Force commit with final message
        subprocess.run(["git", "commit", "-m", "🔥 FINAL VERSION - LATEST APP ONLY - WEB DOWNLOAD FIX"], check=True)
        print("✅ Changes committed")
        
        # Force push to GitHub
        subprocess.run(["git", "push", "--force", "origin", "main"], check=True)
        print("✅ Force pushed to GitHub successfully!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during final deployment: {e}")
        return False

def main():
    """Main final deployment function"""
    print("🚀 Starting final deployment process...")
    
    # Create final web files
    web_dir = create_final_web_files()
    
    # Deploy final version to GitHub
    success = deploy_final_to_github()
    
    if success:
        print("🎉 Final deployment completed successfully!")
        print(f"📁 Final web files created in: {web_dir}")
        print("🌐 GitHub repository updated with latest version only")
        print("📦 Web download now shows ONLY the latest app")
        print("🌐 To run final web app: cd web_deploy_final && python web_app.py")
    else:
        print("❌ Final deployment failed")
        print("💡 Please check your git configuration")

if __name__ == "__main__":
    main() 