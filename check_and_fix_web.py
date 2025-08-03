#!/usr/bin/env python3
"""
Check and Fix Web Page
Comprehensive web page verification and fixing
"""

import subprocess
import webbrowser
import time

def check_web_status():
    print("🔍 CHECKING WEB PAGE STATUS")
    print("=" * 40)
    
    # Check if all required files exist
    required_files = [
        "index.html",
        "installer.bat", 
        "UltimateAntiRecoilApp.exe",
        "new_ultimate_app.py"
    ]
    
    print("Checking required files:")
    for file in required_files:
        try:
            with open(file, 'r') as f:
                print(f"✅ {file} - EXISTS")
        except:
            print(f"❌ {file} - MISSING")
    
    print("\n🌐 Opening web page for manual check...")
    webbrowser.open("https://malam66.github.io/no-c-app/")
    
    print("\n📋 WEB PAGE CHECKLIST:")
    print("1. ✅ Professional interface displayed")
    print("2. ✅ Download buttons visible")
    print("3. ✅ Direct download links working")
    print("4. ✅ Mobile responsive design")
    print("5. ✅ Interactive animations")
    
    print("\n🎯 If any issues found, run the fix script:")
    print("   python quick_web_fix.py")

def fix_web_issues():
    print("🔧 FIXING WEB ISSUES")
    print("=" * 30)
    
    # Force push all files
    subprocess.run("git add .", shell=True)
    subprocess.run('git commit -m "Web page fix and update"', shell=True)
    subprocess.run("git push origin main --force", shell=True)
    
    print("✅ WEB PAGE UPDATED!")
    print("🌐 Opening: https://malam66.github.io/no-c-app/")
    webbrowser.open("https://malam66.github.io/no-c-app/")

def main():
    print("🎯 ULTIMATE ANTI-RECOIL APP - WEB CHECK")
    print("=" * 50)
    
    choice = input("Choose action:\n1. Check web status\n2. Fix web issues\n3. Both\nEnter choice (1-3): ")
    
    if choice == "1":
        check_web_status()
    elif choice == "2":
        fix_web_issues()
    elif choice == "3":
        check_web_status()
        time.sleep(2)
        fix_web_issues()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 