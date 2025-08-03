import subprocess
import webbrowser

def deploy_aim_assist():
    print("🎯 DEPLOYING AIM ASSIST UPDATE")
    print("=" * 40)
    
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    print("Committing aim assist update...")
    subprocess.run('git commit -m "Add aim assist functionality to the app"', shell=True)
    
    print("Pushing to GitHub...")
    subprocess.run("git push origin main", shell=True)
    
    print("✅ AIM ASSIST UPDATE DEPLOYED!")
    print("🌐 Opening web page...")
    webbrowser.open("https://malam66.github.io/no-c-app/")
    
    print("\n🎯 NEW AIM ASSIST FEATURES:")
    print("✅ Aim assist enabled by default")
    print("✅ Auto target detection")
    print("✅ Adjustable aim strength")
    print("✅ Field of view control")
    print("✅ Smooth aim movement")
    print("✅ Target size adjustment")
    print("✅ F4 hotkey to toggle aim assist")
    print("✅ F5 hotkey to test aim assist")

if __name__ == "__main__":
    deploy_aim_assist() 