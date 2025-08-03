import webbrowser
import time

def change_github_link():
    print("🎯 Changing GitHub Repository Link")
    print("=" * 50)
    print()
    print("To change your GitHub Pages link, you need to:")
    print("1. Go to your GitHub repository settings")
    print("2. Change the repository name")
    print("3. Your new link will be: https://malam66.github.io/NEW-NAME/")
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/strong-app/settings")
    
    print()
    print("📋 Steps to change repository name:")
    print("1. Scroll down to 'Repository name' section")
    print("2. Click 'Rename' button")
    print("3. Enter new name (e.g., 'ultimate-auto-script')")
    print("4. Click 'Rename repository'")
    print("5. Confirm the change")
    print()
    
    print("💡 Suggested new names:")
    print("• ultimate-auto-script")
    print("• gaming-utility-app")
    print("• no-recoil-tool")
    print("• auto-script-app")
    print("• gaming-assistant")
    print()
    
    print("✅ After renaming, your new link will be:")
    print("https://malam66.github.io/NEW-NAME/")
    print()
    print("⏳ Wait 5-10 minutes for GitHub Pages to update")
    print("🔄 Clear browser cache if you don't see changes")
    
    input("Press Enter to continue...")

if __name__ == "__main__":
    change_github_link() 