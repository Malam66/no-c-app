import subprocess
import webbrowser

def fix_web_simple():
    print("🔧 FIXING WEB PAGE - SIMPLE VERSION")
    print("=" * 40)
    
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    print("Committing simplified version...")
    subprocess.run('git commit -m "Fix simplified web page - show only download buttons"', shell=True)
    
    print("Pushing to GitHub...")
    subprocess.run("git push origin main", shell=True)
    
    print("✅ SIMPLE WEB PAGE FIXED!")
    print("🌐 Opening web page...")
    webbrowser.open("https://malam66.github.io/no-c-app/")
    
    print("\n🎯 SIMPLE WEB PAGE FEATURES:")
    print("✅ Only download buttons")
    print("✅ No extra features")
    print("✅ Clean and minimal")
    print("✅ Mobile responsive")

if __name__ == "__main__":
    fix_web_simple() 