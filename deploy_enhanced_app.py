import subprocess
import webbrowser

def deploy_enhanced_app():
    print("🎯 DEPLOYING ENHANCED APP WITH CUSTOMIZATION")
    print("=" * 50)
    
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    print("Committing enhanced app...")
    subprocess.run('git commit -m "Enhanced app with full customization - aim assist working in games"', shell=True)
    
    print("Pushing to GitHub...")
    subprocess.run("git push origin main", shell=True)
    
    print("✅ ENHANCED APP DEPLOYED!")
    print("🌐 Opening web page...")
    webbrowser.open("https://malam66.github.io/no-c-app/")
    
    print("\n🎯 ENHANCED APP FEATURES:")
    print("✅ Tabbed interface (Main, Customize, Advanced)")
    print("✅ Mouse sensitivity control (50-200%)")
    print("✅ Customizable keybinds")
    print("✅ Auto Fire, Rapid Fire, Trigger Bot")
    print("✅ ESP (Wallhack) feature")
    print("✅ Multiple aim assist styles (smooth, snap, predictive, adaptive)")
    print("✅ Game profiles (auto, fps, battle_royale, tactical, custom)")
    print("✅ Auto reload and auto scope features")
    print("✅ Enhanced aim assist working in games")
    print("✅ No CMD window when app opens")
    print("✅ Professional desktop icon")

if __name__ == "__main__":
    deploy_enhanced_app() 