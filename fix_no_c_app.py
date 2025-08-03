import webbrowser
import time

def fix_no_c_app():
    print("🎯 Fix Repository Name - no-c-app to anti-recoil-app")
    print("=" * 50)
    print()
    
    print("❌ Current Problem:")
    print("URL: https://malam66.github.io/no-c-app/ (WRONG)")
    print("Content: Shows 'no-c-app' instead of ANTI-RECOIL APP")
    print()
    
    print("✅ Target:")
    print("URL: https://malam66.github.io/anti-recoil-app/ (CORRECT)")
    print("Content: ANTI-RECOIL APP with full functionality")
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/no-c-app/settings")
    
    print()
    print("📋 Fix Instructions:")
    print("1. On the settings page, scroll down to 'Repository name'")
    print("2. Click 'Rename' button next to 'no-c-app'")
    print("3. Change name to: anti-recoil-app")
    print("4. Click 'Rename repository'")
    print("5. Confirm the change")
    print()
    print("✅ This will fix the website")
    print("🌐 New working URL:")
    print("   https://malam66.github.io/anti-recoil-app/")
    print()
    print("⚡ Deployment time: 1 second")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Proceed with fix? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding to fix repository name...")
        print("Go to the opened GitHub page and follow the steps above!")
        print()
        print("🌐 Your working website will be:")
        print("   https://malam66.github.io/anti-recoil-app/")
    else:
        print("✅ Cancelled - website will remain broken")

if __name__ == "__main__":
    fix_no_c_app() 