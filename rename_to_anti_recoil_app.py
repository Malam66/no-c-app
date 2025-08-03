import webbrowser
import time

def rename_to_anti_recoil_app():
    print("🎯 Rename Repository to anti-recoil-app")
    print("=" * 50)
    print()
    
    print("❌ Current Problem:")
    print("URL: https://malam66.github.io/anti-recoil-/ (NOT WORKING)")
    print("Need: https://malam66.github.io/anti-recoil-app/ (WORKING)")
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/ultimate-auto-script/settings")
    
    print()
    print("📋 Rename Instructions:")
    print("1. On the settings page, scroll down to 'Repository name'")
    print("2. Click 'Rename' button next to 'ultimate-auto-script'")
    print("3. Change name to: anti-recoil-app")
    print("4. Click 'Rename repository'")
    print("5. Confirm the change")
    print()
    print("✅ This will fix the URL")
    print("🌐 New working URL:")
    print("   https://malam66.github.io/anti-recoil-app/")
    print()
    print("⚡ Deployment time: 1 second")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Proceed with rename? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding to rename repository...")
        print("Go to the opened GitHub page and follow the steps above!")
        print()
        print("🌐 Your working website will be:")
        print("   https://malam66.github.io/anti-recoil-app/")
    else:
        print("✅ Cancelled - URL will remain broken")

if __name__ == "__main__":
    rename_to_anti_recoil_app() 