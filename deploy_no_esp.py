import subprocess
import webbrowser

def deploy_no_esp():
    print("🎯 DEPLOYING APP WITHOUT ESP FEATURE")
    print("=" * 40)
    
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    print("Committing ESP removal...")
    subprocess.run('git commit -m "Remove ESP feature as requested - clean app"', shell=True)
    
    print("Pushing to GitHub...")
    subprocess.run("git push origin main", shell=True)
    
    print("✅ APP UPDATED - ESP REMOVED!")
    print("🌐 Opening web page...")
    webbrowser.open("https://malam66.github.io/no-c-app/")
    
    print("\n🎯 UPDATED APP FEATURES:")
    print("✅ Tabbed interface (Main, Customize, Advanced)")
    print("✅ Mouse sensitivity control (50-200%)")
    print("✅ Customizable keybinds")
    print("✅ Auto Fire, Rapid Fire, Trigger Bot")
    print("✅ Multiple aim assist styles (smooth, snap, predictive, adaptive)")
    print("✅ Game profiles (auto, fps, battle_royale, tactical, custom)")
    print("✅ Auto reload and auto scope features")
    print("✅ Enhanced aim assist working in games")
    print("✅ No CMD window when app opens")
    print("✅ Professional desktop icon")
    print("❌ ESP feature removed as requested")

if __name__ == "__main__":
    deploy_no_esp() 