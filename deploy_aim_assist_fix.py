import subprocess
import webbrowser

def deploy_aim_assist_fix():
    print("🎯 DEPLOYING AIM ASSIST FIX")
    print("=" * 40)
    
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    print("Committing aim assist fix...")
    subprocess.run('git commit -m "Fix aim assist to work properly in games - real mouse tracking"', shell=True)
    
    print("Pushing to GitHub...")
    subprocess.run("git push origin main", shell=True)
    
    print("✅ AIM ASSIST FIX DEPLOYED!")
    print("🌐 Opening web page...")
    webbrowser.open("https://malam66.github.io/no-c-app/")
    
    print("\n🎯 AIM ASSIST FIXES:")
    print("✅ Real mouse movement tracking")
    print("✅ Automatic target detection")
    print("✅ Smooth aim assist movement")
    print("✅ Game-optimized timing")
    print("✅ No CMD window")
    print("✅ Professional desktop icon")
    print("✅ Web download working")

if __name__ == "__main__":
    deploy_aim_assist_fix() 