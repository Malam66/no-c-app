import webbrowser
import subprocess
import os

def check_website_status():
    """Quickly check website status"""
    
    print("⚡ QUICK WEBSITE CHECK")
    print("=" * 50)
    
    print("\n🌐 CHECKING WEBSITE NOW:")
    print("URL: https://malam66.github.io/strong-app/")
    
    # Open website in browser
    print("\n🚀 Opening website...")
    webbrowser.open('https://malam66.github.io/strong-app/')
    
    print("\n📋 WHAT TO LOOK FOR:")
    print("✅ Should show: Strong No Recoil website with download button")
    print("❌ Still shows: Just 'strong-app' text")
    
    print("\n🔧 IF STILL NOT WORKING:")
    print("1. Clear browser cache (Ctrl + Shift + Delete)")
    print("2. Try incognito mode (Ctrl + Shift + N)")
    print("3. Check GitHub Pages settings")
    
    # Open GitHub Pages settings
    print("\n🔧 Opening GitHub Pages settings...")
    webbrowser.open('https://github.com/Malam66/strong-app/settings/pages')
    
    print("\n📝 QUICK FIX:")
    print("If website still shows 'strong-app':")
    print("1. Go to GitHub Pages settings")
    print("2. Select 'Deploy from a branch'")
    print("3. Choose 'main' branch")
    print("4. Click 'Save'")
    
    print("\n⏰ Deployment should be instant now!")

if __name__ == "__main__":
    check_website_status() 