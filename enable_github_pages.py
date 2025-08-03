import webbrowser
import time

def enable_github_pages():
    print("🎯 GitHub Pages Enable Guide")
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
    print("4. Under 'Branch', select 'master'")
    print("5. Under 'Folder', select '/' (root)")
    print("6. Click 'Save'")
    print()
    print("✅ This will enable GitHub Pages")
    print("🌐 Your website will be accessible at:")
    print("   https://malam66.github.io/ultimate-auto-script/")
    print()
    print("⏳ Wait 5-10 minutes for the website to deploy")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Do you want to proceed? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding to enable GitHub Pages...")
        print("Go to the opened GitHub page and follow the steps above!")
        print()
        print("🌐 Your website will be live at:")
        print("   https://malam66.github.io/ultimate-auto-script/")
    else:
        print("✅ Cancelled - GitHub Pages will remain disabled")

if __name__ == "__main__":
    enable_github_pages() 