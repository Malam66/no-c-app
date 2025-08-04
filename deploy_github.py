#!/usr/bin/env python3
"""
GitHub Deployment Script for Ultimate Gaming App
Deploys the app to GitHub with proper documentation
"""

import os
import shutil
import subprocess
import sys

def create_github_files():
    """Create GitHub deployment files"""
    print("📦 Creating GitHub deployment files...")
    
    # Create README.md
    readme_content = """# 🎯 Ultimate Gaming App

A powerful gaming application with anti-recoil and aim assist features.

## ✨ Features

- **🔫 Anti-Recoil**: Automatic recoil compensation
- **🎯 Improved Aim Assist**: Better tracking with less shaking
- **🛡️ Mouse Control Protection**: Full user control priority
- **⏳ Startup Protection**: 10-second startup delay
- **🎮 Works in All Games**: Universal compatibility

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ultimate-gaming-app.git
cd ultimate-gaming-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python new_ultimate_app.py
```

## 🎮 How to Use

### Anti-Recoil
- Hold mouse button for automatic recoil compensation
- Adjust strength in the app settings
- Works with all games

### Aim Assist
- Automatically detects enemy movement
- Provides precise aim assistance
- Reduced shaking for better control

### Controls
- **Hold Mouse Button**: Anti-recoil
- **Press SPACE**: Manual anti-recoil
- **Press F2**: Test anti-recoil
- **Press F5**: Test aim assist
- **CAPS LOCK**: Master switch

## ⚙️ Settings

- **Aimdown**: Recoil compensation strength (1-25)
- **Smoothness**: Movement smoothness (5-25)
- **Delay**: Time between movements (0.01-0.15s)
- **Aim Assist Strength**: Aim assist power (1-50)

## 🛡️ Safety Features

- **Startup Protection**: 10-second delay prevents immediate activation
- **Mouse Control Priority**: Your mouse movements take full priority
- **Error Handling**: Automatic error recovery
- **Graceful Shutdown**: Clean app closing

## 📁 Files

- `new_ultimate_app.py`: Main application
- `requirements.txt`: Python dependencies
- `deploy_web.py`: Web deployment script
- `deploy_github.py`: GitHub deployment script

## 🌐 Web Deployment

To deploy to web:

```bash
python deploy_web.py
cd web_deploy
python web_app.py
```

Then visit: http://localhost:5000

## 📝 License

This project is for educational purposes only.

## ⚠️ Disclaimer

This app is for educational and testing purposes. Use responsibly and in accordance with game terms of service.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For support, create an issue on GitHub.

---

**🎯 Ultimate Gaming App - Complete Fix**
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# App specific
*.log
temp/
cache/
"""

    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    # Create GitHub Actions workflow
    os.makedirs(".github/workflows", exist_ok=True)
    
    workflow_content = """name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        
    - name: Run tests
      run: |
        python -c "import tkinter; print('Tkinter available')"
        python -c "import pynput; print('Pynput available')"
        
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      if: github.ref == 'refs/heads/main'
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./web_deploy
"""

    with open(".github/workflows/deploy.yml", "w") as f:
        f.write(workflow_content)
    
    print("✅ GitHub files created successfully!")

def deploy_to_github():
    """Deploy to GitHub"""
    print("📦 Deploying to GitHub...")
    
    try:
        # Initialize git if not already done
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], check=True)
            print("✅ Git repository initialized")
        
        # Add all files
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Files added to git")
        
        # Commit changes
        subprocess.run(["git", "commit", "-m", "Ultimate Gaming App - Complete Fix with Web Deployment"], check=True)
        print("✅ Changes committed")
        
        # Add remote if not exists
        try:
            subprocess.run(["git", "remote", "add", "origin", "https://github.com/yourusername/ultimate-gaming-app.git"], check=True)
            print("✅ Remote origin added")
        except subprocess.CalledProcessError:
            print("ℹ️ Remote origin already exists")
        
        # Push to GitHub
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Pushed to GitHub successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during GitHub deployment: {e}")
        print("💡 Make sure you have git configured and have access to the repository")
        return False
    
    return True

def create_release_package():
    """Create a release package"""
    print("📦 Creating release package...")
    
    release_dir = "release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # Copy main files
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
    
    # Create installer script
    installer_content = """@echo off
echo Installing Ultimate Gaming App...
pip install -r requirements.txt
echo Installation complete!
echo Run: python new_ultimate_app.py
pause
"""
    
    with open(os.path.join(release_dir, "install.bat"), "w") as f:
        f.write(installer_content)
    
    print("✅ Release package created in 'release' directory")
    return release_dir

def main():
    """Main deployment function"""
    print("🚀 Starting GitHub deployment process...")
    
    # Create GitHub files
    create_github_files()
    
    # Create release package
    release_dir = create_release_package()
    
    # Deploy to GitHub
    success = deploy_to_github()
    
    if success:
        print("🎉 GitHub deployment completed successfully!")
        print(f"📁 Release package created in: {release_dir}")
        print("🌐 GitHub repository: https://github.com/yourusername/ultimate-gaming-app")
        print("📦 To create a release, go to GitHub and create a new release")
    else:
        print("❌ GitHub deployment failed")
        print("💡 Please check your git configuration and repository access")

if __name__ == "__main__":
    main() 