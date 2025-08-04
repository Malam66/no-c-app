import webbrowser
import time

def deploy_anti_recoil_app():
    print("🎯 Deploy Anti-Recoil App to GitHub Pages")
    print("=" * 50)
    print()
    
    print("🌐 Target URL:")
    print("   https://malam66.github.io/anti-recoil-app/")
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/ultimate-auto-script/settings/pages")
    
    print()
    print("📋 Deployment Instructions:")
    print("1. On the settings page, scroll down to 'Pages' section")
    print("2. Under 'Source', select 'Deploy from a branch'")
    print("3. Under 'Branch', select 'master'")
    print("4. Under 'Folder', select '/' (root)")
    print("5. Click 'Save'")
    print()
    print("🔄 Then rename repository:")
    print("6. Go to 'Repository name' section")
    print("7. Click 'Rename' button")
    print("8. Change name to: anti-recoil-app")
    print("9. Click 'Rename repository'")
    print("10. Confirm the change")
    print()
    print("✅ This will deploy your website")
    print("🌐 Working URL:")
    print("   https://malam66.github.io/anti-recoil-app/")
    print()
    print("⚡ Deployment time: 1 second")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Proceed with deployment? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding with deployment...")
        print("Go to the opened GitHub page and follow the steps above!")
        print()
        print("🌐 Your website will be live at:")
        print("   https://malam66.github.io/anti-recoil-app/")
    else:
        print("✅ Cancelled - deployment not started")

if __name__ == "__main__":
    deploy_anti_recoil_app() 