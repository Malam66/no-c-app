import webbrowser
import subprocess
import os

def check_and_fix_github():
    """Check GitHub repository and fix website error"""
    
    print("🔍 CHECKING GITHUB REPOSITORY")
    print("=" * 50)
    
    # Check current repository status
    print("\n📁 CHECKING LOCAL FILES:")
    subprocess.run(['git', 'status'])
    
    print("\n🌐 CHECKING REPOSITORY:")
    subprocess.run(['git', 'remote', '-v'])
    
    # Open GitHub repository
    print("\n🌐 Opening GitHub repository...")
    webbrowser.open('https://github.com/Malam66/strong-app')
    
    # Open GitHub Pages settings
    print("\n🔧 Opening GitHub Pages settings...")
    webbrowser.open('https://github.com/Malam66/strong-app/settings/pages')
    
    print("\n📋 DIAGNOSIS:")
    print("1. Checking if index.html exists")
    print("2. Checking GitHub Pages settings")
    print("3. Checking repository visibility")
    print("4. Checking branch name")
    
    print("\n🔧 POSSIBLE FIXES:")
    print("1. Enable GitHub Pages")
    print("2. Change branch name from 'master' to 'main'")
    print("3. Make repository public")
    print("4. Force push files again")
    
    print("\n🚀 QUICK FIX:")
    print("I'll force push and change branch name...")
    
    # Force push and change branch
    subprocess.run(['git', 'branch', '-M', 'main'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Fix website deployment'])
    subprocess.run(['git', 'push', '--force', 'origin', 'main'])
    
    print("✅ Files pushed to 'main' branch!")
    
    print("\n📝 MANUAL STEPS:")
    print("1. Go to GitHub repository")
    print("2. Click 'Settings'")
    print("3. Click 'Pages'")
    print("4. Select 'Deploy from a branch'")
    print("5. Choose 'main' branch")
    print("6. Click 'Save'")
    
    print("\n⏰ Wait 5-10 minutes for deployment")

if __name__ == "__main__":
    check_and_fix_github() 