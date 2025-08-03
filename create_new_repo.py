import webbrowser
import subprocess
import os

def create_new_repository():
    """Create a new GitHub repository for the website"""
    
    print("🚀 CREATE NEW GITHUB REPOSITORY")
    print("=" * 50)
    
    print("\n📋 NEW REPOSITORY OPTIONS:")
    print("1. no-recoil-app")
    print("2. gaming-utility")
    print("3. recoil-control")
    print("4. strong-app")
    print("5. no-recoil-tool")
    print("6. Custom name")
    
    # Open GitHub new repository page
    print("\n🌐 Opening GitHub new repository page...")
    webbrowser.open('https://github.com/new')
    
    print("\n📝 STEPS TO CREATE NEW REPOSITORY:")
    print("1. Repository name: Choose from above or custom")
    print("2. Make it PUBLIC ✅")
    print("3. Don't check 'Add a README file'")
    print("4. Click 'Create repository'")
    print("5. Copy the repository URL")
    
    print("\n🔗 YOUR NEW WEBSITE URL WILL BE:")
    print("https://malam66.github.io/NEW-REPO-NAME/")
    
    print("\n📁 AFTER CREATING REPOSITORY:")
    print("1. Run: git remote set-url origin https://github.com/Malam66/NEW-REPO-NAME.git")
    print("2. Run: git push -u origin master")
    print("3. Enable GitHub Pages in Settings > Pages")
    
    print("\n💡 RECOMMENDED NAMES:")
    print("- no-recoil-app (clean and professional)")
    print("- gaming-utility (generic and safe)")
    print("- recoil-control (descriptive)")

if __name__ == "__main__":
    create_new_repository() 