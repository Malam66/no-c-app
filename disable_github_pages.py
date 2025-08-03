import webbrowser
import time

def disable_github_pages():
    print("🎯 GitHub Pages Disable Guide")
    print("=" * 50)
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/ultimate-auto-script/settings/pages")
    
    print()
    print("📋 Step-by-Step Instructions:")
    print("1. On the settings page, scroll down to 'Pages' section")
    print("2. Under 'Source', click the dropdown menu")
    print("3. Select 'Deploy from a branch'")
    print("4. Under 'Branch', select 'None'")
    print("5. Click 'Save'")
    print()
    print("✅ This will disable GitHub Pages")
    print("❌ Your website will no longer be accessible")
    print()
    print("⏳ The website will be disabled immediately")
    print("🔄 You can re-enable it later if needed")
    print()
    
    choice = input("Do you want to proceed? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding to disable GitHub Pages...")
        print("Go to the opened GitHub page and follow the steps above!")
    else:
        print("✅ Cancelled - GitHub Pages will remain active")

if __name__ == "__main__":
    disable_github_pages() 