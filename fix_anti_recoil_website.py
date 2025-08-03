import webbrowser
import time

def fix_anti_recoil_website():
    print("🎯 Fix Anti-Recoil Website")
    print("=" * 50)
    print()
    
    print("❌ Current Issue:")
    print("Website shows only '# anti-recoil-'")
    print("URL: https://malam66.github.io/anti-recoil-/")
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/ultimate-auto-script/settings")
    
    print()
    print("📋 Fix Instructions:")
    print("1. On the settings page, scroll down to 'Repository name'")
    print("2. Click 'Rename' button")
    print("3. Change name to: anti-recoil-app")
    print("4. Click 'Rename repository'")
    print("5. Go to Pages settings")
    print("6. Set Source to 'Deploy from a branch'")
    print("7. Set Branch to 'master'")
    print("8. Set Folder to '/' (root)")
    print("9. Click 'Save'")
    print()
    print("✅ This will fix the website")
    print("🌐 New URL will be:")
    print("   https://malam66.github.io/anti-recoil-app/")
    print()
    print("⚡ Deployment time: 1 second")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Proceed with fix? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding to fix website...")
        print("Go to the opened GitHub page and follow the steps above!")
        print()
        print("🌐 New website URL:")
        print("   https://malam66.github.io/anti-recoil-app/")
    else:
        print("✅ Cancelled - website will remain broken")

if __name__ == "__main__":
    fix_anti_recoil_website() 