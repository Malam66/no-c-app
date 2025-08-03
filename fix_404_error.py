import webbrowser
import time

def fix_404_error():
    print("🎯 Fix 404 Error - Enable GitHub Pages")
    print("=" * 50)
    print()
    
    print("❌ Current Problem:")
    print("URL: https://malam66.github.io/anti-recoil-app/")
    print("Error: 404 Not Found - There isn't a GitHub Pages site here")
    print()
    
    print("✅ Solutions:")
    print("1. Check current repository name")
    print("2. Enable GitHub Pages")
    print("3. Fix repository settings")
    print()
    
    # Open GitHub repository settings
    print("Opening GitHub repository settings...")
    webbrowser.open("https://github.com/Malam66/ultimate-auto-script/settings/pages")
    
    print()
    print("📋 Fix Instructions:")
    print("1. Check if repository exists:")
    print("   - Go to: https://github.com/Malam66/")
    print("   - Look for your repository name")
    print()
    print("2. Enable GitHub Pages:")
    print("   - On settings page, scroll to 'Pages'")
    print("   - Under 'Source', select 'Deploy from a branch'")
    print("   - Under 'Branch', select 'master'")
    print("   - Under 'Folder', select '/' (root)")
    print("   - Click 'Save'")
    print()
    print("3. Rename repository (if needed):")
    print("   - Go to 'Repository name' section")
    print("   - Click 'Rename' button")
    print("   - Change to: anti-recoil-app")
    print("   - Click 'Rename repository'")
    print()
    print("✅ This will fix the 404 error")
    print("🌐 Working URL:")
    print("   https://malam66.github.io/anti-recoil-app/")
    print()
    print("⚡ Deployment time: 1 second")
    print("🔄 Clear browser cache if needed")
    print()
    
    choice = input("Proceed with fix? (y/n): ")
    
    if choice.lower() == 'y':
        print("✅ Proceeding to fix 404 error...")
        print("Go to the opened GitHub page and follow the steps above!")
        print()
        print("🌐 Your working website will be:")
        print("   https://malam66.github.io/anti-recoil-app/")
    else:
        print("✅ Cancelled - 404 error will remain")

if __name__ == "__main__":
    fix_404_error() 