#!/usr/bin/env python3
"""
GitHub Deployment Script for Ultimate Anti-Recoil App
Automates the process of preparing and deploying to GitHub
"""

import os
import subprocess
import shutil
import json
from datetime import datetime

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None

def create_release_files():
    """Create files needed for GitHub release"""
    print("📦 Creating release files...")
    
    # Create release directory
    release_dir = "release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # Copy essential files
    essential_files = [
        "new_ultimate_app.py",
        "ultimate_app_final.py", 
        "setup.py",
        "installer.bat",
        "create_nice_icon.py",
        "web_installer.html",
        "requirements.txt",
        "README.md",
        "LICENSE",
        ".gitignore"
    ]
    
    for file in essential_files:
        if os.path.exists(file):
            shutil.copy2(file, release_dir)
            print(f"📄 Copied {file}")
    
    # Copy icon files if they exist
    icon_files = ["app_icon.ico", "app_icon.png"]
    for icon in icon_files:
        if os.path.exists(icon):
            shutil.copy2(icon, release_dir)
            print(f"🎨 Copied {icon}")
    
    # Copy built executable if it exists
    exe_path = "build/exe.win-amd64-3.11/UltimateAntiRecoilApp.exe"
    if os.path.exists(exe_path):
        shutil.copy2(exe_path, release_dir)
        print(f"🚀 Copied executable")
    
    print(f"✅ Release files created in {release_dir}/")

def create_github_workflow():
    """Create GitHub Actions workflow for automated builds"""
    workflow_dir = ".github/workflows"
    os.makedirs(workflow_dir, exist_ok=True)
    
    workflow_content = '''name: Build and Release

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pynput keyboard mouse cx_Freeze Pillow
    
    - name: Create icon
      run: python create_nice_icon.py
    
    - name: Build executable
      run: python setup.py build
    
    - name: Create installer
      run: .\\installer.bat
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: UltimateAntiRecoilApp
        path: |
          build/exe.win-amd64-3.11/
          installer.bat
          app_icon.ico
          app_icon.png
        retention-days: 30
    
    - name: Create Release
      if: startsWith(github.ref, 'refs/tags/')
      uses: softprops/action-gh-release@v1
      with:
        files: |
          build/exe.win-amd64-3.11/UltimateAntiRecoilApp.exe
          installer.bat
          app_icon.ico
          app_icon.png
        draft: false
        prerelease: false
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
'''
    
    with open(f"{workflow_dir}/build.yml", "w") as f:
        f.write(workflow_content)
    
    print("✅ GitHub Actions workflow created")

def create_package_json():
    """Create package.json for GitHub repository metadata"""
    package_data = {
        "name": "ultimate-anti-recoil-app",
        "version": "2.0.0",
        "description": "Professional Windows anti-recoil application with GUI and desktop integration",
        "main": "new_ultimate_app.py",
        "scripts": {
            "start": "python new_ultimate_app.py",
            "build": "python setup.py build",
            "install": "installer.bat",
            "icon": "python create_nice_icon.py"
        },
        "keywords": [
            "anti-recoil",
            "gaming",
            "windows",
            "python",
            "tkinter",
            "mouse-control"
        ],
        "author": "Your Name",
        "license": "MIT",
        "repository": {
            "type": "git",
            "url": "https://github.com/yourusername/ultimate-anti-recoil-app.git"
        },
        "bugs": {
            "url": "https://github.com/yourusername/ultimate-anti-recoil-app/issues"
        },
        "homepage": "https://github.com/yourusername/ultimate-anti-recoil-app#readme"
    }
    
    with open("package.json", "w") as f:
        json.dump(package_data, f, indent=2)
    
    print("✅ package.json created")

def create_github_pages():
    """Create GitHub Pages configuration"""
    pages_content = '''# Ultimate Anti-Recoil App

Welcome to the Ultimate Anti-Recoil App GitHub Pages!

## 🚀 Quick Download

[Download Installer](installer.bat)

[Download Executable](build/exe.win-amd64-3.11/UltimateAntiRecoilApp.exe)

## 📋 Features

- 🎮 Advanced anti-recoil system
- 🖥️ Beautiful GUI interface
- 🚀 Silent execution (no CMD window)
- 🖱️ Desktop shortcut with custom icon
- 📦 Easy installation process

## 🛠️ Installation

1. Download the installer
2. Run as administrator
3. Enjoy your new desktop shortcut!

## 📞 Support

For issues and questions, please visit our [GitHub repository](https://github.com/yourusername/ultimate-anti-recoil-app).
'''
    
    with open("docs/index.md", "w", encoding='utf-8') as f:
        f.write(pages_content)
    
    print("✅ GitHub Pages content created")

def deploy_to_github():
    """Deploy the app to GitHub"""
    print("🚀 Deploying to GitHub...")
    
    # Create release directory
    if not os.path.exists("release"):
        os.makedirs("release")
    
    # Copy main app file
    shutil.copy("new_ultimate_app.py", "release/")
    
    # Copy requirements
    if os.path.exists("requirements.txt"):
        shutil.copy("requirements.txt", "release/")
    
    # Copy setup files
    if os.path.exists("setup.py"):
        shutil.copy("setup.py", "release/")
    
    # Copy README
    if os.path.exists("README.md"):
        shutil.copy("README.md", "release/")
    
    # Copy license
    if os.path.exists("LICENSE"):
        shutil.copy("LICENSE", "release/")
    
    # Copy icons
    if os.path.exists("app_icon.ico"):
        shutil.copy("app_icon.ico", "release/")
    if os.path.exists("app_icon.png"):
        shutil.copy("app_icon.png", "release/")
    
    # Create web installer
    web_installer = """<!DOCTYPE html>
<html>
<head>
    <title>Ultimate Gaming App - Download</title>
    <style>
        body { font-family: Arial, sans-serif; background: #1a1a1a; color: #ffffff; text-align: center; padding: 50px; }
        .container { max-width: 600px; margin: 0 auto; background: #2a2a2a; padding: 30px; border-radius: 10px; }
        .download-btn { background: #00ff00; color: #000000; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; margin: 10px; display: inline-block; }
        .feature { background: #333333; padding: 15px; margin: 10px 0; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎯 Ultimate Gaming App</h1>
        <p>Complete gaming assistant with anti-recoil and aim assist</p>
        
        <div class="feature">
            <h3>🔫 Anti-Recoil</h3>
            <p>Hold mouse button for automatic recoil compensation</p>
        </div>
        
        <div class="feature">
            <h3>🎯 Improved Aim Assist</h3>
            <p>Better tracking with less shaking</p>
        </div>
        
        <div class="feature">
            <h3>⚙️ Customizable Settings</h3>
            <p>Adjust strength, smoothness, and timing</p>
        </div>
        
        <a href="new_ultimate_app.py" class="download-btn">📥 Download App</a>
        <a href="requirements.txt" class="download-btn">📦 Download Requirements</a>
        <a href="setup.py" class="download-btn">🔧 Download Setup</a>
        
        <h3>Installation:</h3>
        <p>1. Download all files</p>
        <p>2. Install Python requirements: pip install -r requirements.txt</p>
        <p>3. Run the app: python new_ultimate_app.py</p>
    </div>
</body>
</html>"""
    
    with open("release/web_installer.html", "w") as f:
        f.write(web_installer)
    
    print("✅ Files prepared for GitHub deployment")
    print("📁 Release directory created with all files")
    print("🌐 Web installer created")
    
    # Git commands
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Deploy Ultimate Gaming App"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Successfully deployed to GitHub!")
    except subprocess.CalledProcessError:
        print("⚠️ Git commands failed - please check your Git setup")
        print("📁 Files are ready in the 'release' directory")

def main():
    """Main deployment function"""
    print("🚀 Starting GitHub deployment preparation...")
    print("=" * 50)
    
    # Create release files
    create_release_files()
    
    # Create GitHub Actions workflow
    create_github_workflow()
    
    # Create package.json
    create_package_json()
    
    # Create GitHub Pages
    os.makedirs("docs", exist_ok=True)
    create_github_pages()
    
    # Git commands for deployment
    print("\n📝 Git commands to run:")
    print("=" * 50)
    print("git add .")
    print("git commit -m 'Initial release: Ultimate Anti-Recoil App v2.0.0'")
    print("git tag -a v2.0.0 -m 'Release v2.0.0'")
    print("git push origin main")
    print("git push origin v2.0.0")
    print("=" * 50)
    
    print("\n🎉 Deployment preparation complete!")
    print("📋 Next steps:")
    print("1. Create a new repository on GitHub")
    print("2. Run the git commands above")
    print("3. Enable GitHub Pages in repository settings")
    print("4. Enable GitHub Actions in repository settings")
    print("5. Update the repository URL in package.json and README.md")

if __name__ == "__main__":
    main() 