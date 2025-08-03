import webbrowser
import subprocess
import os

def fix_github_pages():
    """Fix GitHub Pages deployment"""
    
    print("🔧 FIXING GITHUB PAGES")
    print("=" * 50)
    
    print("\n❌ PROBLEM:")
    print("Website shows 'strong-app' instead of full website")
    print("This means GitHub Pages isn't using your index.html")
    
    print("\n🔧 SOLUTIONS:")
    print("1. Enable GitHub Pages")
    print("2. Force refresh deployment")
    print("3. Check repository settings")
    
    # Open GitHub repository settings
    print("\n🌐 Opening GitHub repository settings...")
    webbrowser.open('https://github.com/Malam66/strong-app/settings/pages')
    
    print("\n📝 STEPS TO FIX:")
    print("1. Click 'Pages' in the left menu")
    print("2. Under 'Source', select 'Deploy from a branch'")
    print("3. Choose 'main' branch")
    print("4. Click 'Save'")
    print("5. Wait 5-10 minutes for deployment")
    
    print("\n🔄 ALTERNATIVE: Force Push")
    print("If the above doesn't work, I can force push the files again")
    
    print("\n⏰ TIMELINE:")
    print("- 2 minutes: Enable GitHub Pages")
    print("- 5-10 minutes: Wait for deployment")
    print("- Website should show full content")

if __name__ == "__main__":
    fix_github_pages() 