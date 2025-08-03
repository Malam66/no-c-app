import webbrowser
import subprocess
import os

def create_and_deploy():
    """Create repository and deploy website"""
    
    print("🚀 CREATE AND DEPLOY NEW WEBSITE")
    print("=" * 50)
    
    print("\n📋 REPOSITORY OPTIONS:")
    print("1. no-recoil-app")
    print("2. gaming-utility")
    print("3. recoil-control")
    print("4. strong-app")
    print("5. no-recoil-tool")
    
    print("\n🎯 RECOMMENDED: no-recoil-app")
    
    # Open GitHub to create repository
    print("\n🌐 Opening GitHub to create repository...")
    webbrowser.open('https://github.com/new')
    
    print("\n📝 STEPS:")
    print("1. Repository name: no-recoil-app")
    print("2. Make it PUBLIC ✅")
    print("3. Don't add README")
    print("4. Click 'Create repository'")
    print("5. Tell me the exact name you used!")
    
    print("\n⏰ After creating, I'll deploy it for you!")

if __name__ == "__main__":
    create_and_deploy() 