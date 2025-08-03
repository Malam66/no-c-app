import webbrowser
import time

def rename_repository_guide():
    print("🎯 GitHub Repository Rename Guide")
    print("=" * 50)
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/strong-app/settings")
    
    print()
    print("📋 Step-by-Step Instructions:")
    print("1. On the settings page, scroll down to 'Repository name'")
    print("2. Click the 'Rename' button next to 'strong-app'")
    print("3. Enter one of these names:")
    print()
    print("   💡 Suggested Names:")
    print("   • ultimate-auto-script")
    print("   • gaming-utility-app") 
    print("   • no-recoil-tool")
    print("   • auto-script-app")
    print("   • gaming-assistant")
    print()
    print("4. Click 'Rename repository'")
    print("5. Confirm the change")
    print()
    print("✅ Your new link will be:")
    print("   https://malam66.github.io/NEW-NAME/")
    print()
    print("⏳ Wait 5-10 minutes for GitHub Pages to update")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Which name do you want to use? (or press Enter to skip): ")
    
    if choice:
        print(f"✅ You chose: {choice}")
        print(f"Your new link will be: https://malam66.github.io/{choice}/")
        print()
        print("Now go to the opened GitHub page and rename your repository!")
    else:
        print("✅ Go to the opened GitHub page and choose your own name!")

if __name__ == "__main__":
    rename_repository_guide() 