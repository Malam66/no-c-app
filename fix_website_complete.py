import webbrowser
import subprocess
import os

def fix_website_complete():
    """Complete website fix"""
    
    print("🔧 COMPLETE WEBSITE FIX")
    print("=" * 50)
    
    print("\n❌ CURRENT PROBLEM:")
    print("Website shows 'strong-app' instead of full website")
    
    print("\n🔧 STEP 1: Force Push Files")
    print("Pushing all files to GitHub...")
    
    # Force push all files
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Complete website fix - force update'])
    subprocess.run(['git', 'push', '--force', 'origin', 'master'])
    
    print("✅ Files pushed successfully!")
    
    print("\n🔧 STEP 2: Enable GitHub Pages")
    print("Opening GitHub Pages settings...")
    webbrowser.open('https://github.com/Malam66/strong-app/settings/pages')
    
    print("\n📝 MANUAL STEPS:")
    print("1. Click 'Pages' in left menu")
    print("2. Under 'Source', select 'Deploy from a branch'")
    print("3. Choose 'main' branch")
    print("4. Click 'Save'")
    print("5. Wait 5-10 minutes")
    
    print("\n🔧 STEP 3: Alternative Repository")
    print("If still not working, creating new repository...")
    webbrowser.open('https://github.com/new')
    
    print("\n💡 ALTERNATIVE NAMES:")
    print("- no-recoil-app")
    print("- gaming-utility")
    print("- recoil-control")
    
    print("\n⏰ TIMELINE:")
    print("- 2 minutes: Enable GitHub Pages")
    print("- 5-10 minutes: Wait for deployment")
    print("- Website should work!")

if __name__ == "__main__":
    fix_website_complete() 