#!/usr/bin/env python3
"""
Web Deployment Script for Ultimate Gaming App
Deploys the app to web platforms
"""

import os
import shutil
import subprocess
import sys

def create_web_files():
    """Create web deployment files"""
    print("🌐 Creating web deployment files...")
    
    # Create web directory
    web_dir = "web_deploy"
    if os.path.exists(web_dir):
        shutil.rmtree(web_dir)
    os.makedirs(web_dir)
    
    # Copy main app file
    shutil.copy("new_ultimate_app.py", os.path.join(web_dir, "app.py"))
    
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
    
    # Create web app wrapper
    web_app_code = '''from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_app', methods=['POST'])
def start_app():
    try:
        # Start the app in background
        subprocess.Popen([sys.executable, 'app.py'])
        return jsonify({"status": "success", "message": "App started successfully"})
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
    
    # Create HTML template
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Gaming App - Web Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: white;
        }
        .container {
            max-width: 800px;
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
        .status {
            background: rgba(0,255,0,0.2);
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Ultimate Gaming App - Web Interface</h1>
        
        <div class="feature">
            <h3>🔫 Anti-Recoil</h3>
            <p>Hold mouse button for automatic recoil compensation</p>
        </div>
        
        <div class="feature">
            <h3>🎯 Improved Aim Assist</h3>
            <p>Better tracking with less shaking</p>
        </div>
        
        <div class="feature">
            <h3>⚙️ Features</h3>
            <ul>
                <li>Anti-recoil system</li>
                <li>Improved aim assist</li>
                <li>Mouse control protection</li>
                <li>Startup protection</li>
            </ul>
        </div>
        
        <div style="text-align: center;">
            <button class="button" onclick="startApp()">🚀 Start App</button>
            <button class="button" onclick="downloadApp()">📥 Download App</button>
        </div>
        
        <div id="status" class="status" style="display: none;">
            <p id="statusText">Ready to start...</p>
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
        
        function downloadApp() {
            window.location.href = '/download';
        }
    </script>
</body>
</html>
'''
    
    with open(os.path.join(templates_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print("✅ Web deployment files created successfully!")
    return web_dir

def deploy_to_github():
    """Deploy to GitHub"""
    print("📦 Deploying to GitHub...")
    
    # Initialize git if not already done
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
    
    # Add all files
    subprocess.run(["git", "add", "."])
    
    # Commit changes
    subprocess.run(["git", "commit", "-m", "Ultimate Gaming App - Complete Fix"])
    
    # Add remote if not exists
    try:
        subprocess.run(["git", "remote", "add", "origin", "https://github.com/yourusername/ultimate-gaming-app.git"])
    except:
        pass
    
    # Push to GitHub
    subprocess.run(["git", "push", "-u", "origin", "main"])
    
    print("✅ Deployed to GitHub successfully!")

def main():
    """Main deployment function"""
    print("🚀 Starting deployment process...")
    
    # Create web files
    web_dir = create_web_files()
    
    # Deploy to GitHub
    deploy_to_github()
    
    print("🎉 Deployment completed successfully!")
    print(f"📁 Web files created in: {web_dir}")
    print("🌐 To run web app: cd web_deploy && python web_app.py")

if __name__ == "__main__":
    main() 