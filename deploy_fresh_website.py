import webbrowser
import subprocess
import os

def deploy_fresh_website():
    """Deploy website to a new repository with fresh URL"""
    
    print("🌐 DEPLOYING FRESH WEBSITE")
    print("=" * 50)
    
    # Suggest new repository names
    new_names = [
        "no-recoil-app",
        "gaming-utility", 
        "recoil-control",
        "strong-app",
        "no-recoil-tool",
        "gaming-tool",
        "recoil-utility"
    ]
    
    print("\n💡 SUGGESTED NEW REPOSITORY NAMES:")
    for i, name in enumerate(new_names, 1):
        print(f"{i}. {name}")
    
    print("\n🎯 RECOMMENDED: no-recoil-app")
    print("   This will give you: https://malam66.github.io/no-recoil-app/")
    
    # Open GitHub to create new repository
    print("\n🌐 Opening GitHub to create new repository...")
    webbrowser.open('https://github.com/new')
    
    print("\n📝 QUICK STEPS:")
    print("1. Repository name: no-recoil-app")
    print("2. Make it PUBLIC ✅")
    print("3. Don't add README")
    print("4. Click 'Create repository'")
    print("5. Tell me when done!")
    
    print("\n🚀 AFTER CREATING REPOSITORY:")
    print("I'll help you deploy with these commands:")
    print("- git remote set-url origin https://github.com/Malam66/no-recoil-app.git")
    print("- git push -u origin master")
    print("- Enable GitHub Pages")
    
    print("\n⏰ TIMELINE:")
    print("- 2 minutes: Create repository")
    print("- 3 minutes: Deploy files")
    print("- 5 minutes: Website live!")

if __name__ == "__main__":
    deploy_fresh_website() 