#!/usr/bin/env python3
"""
Quick Web Fix - Add missing files and deploy
"""

import subprocess
import os

def quick_fix():
    print("🔧 QUICK WEB FIX")
    print("=" * 20)
    
    # Copy executable if it exists
    if os.path.exists("build/exe.win-amd64-3.11/UltimateAntiRecoilApp.exe"):
        print("Copying executable...")
        subprocess.run("copy build\\exe.win-amd64-3.11\\UltimateAntiRecoilApp.exe UltimateAntiRecoilApp.exe", shell=True)
    
    # Add all files
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    # Commit
    print("Committing...")
    subprocess.run('git commit -m "Fix web downloads"', shell=True)
    
    # Push
    print("Pushing...")
    subprocess.run("git push origin main", shell=True)
    
    print("✅ WEB FIXED!")
    print("🌐 Opening: https://malam66.github.io/no-c-app/")
    subprocess.run("start https://malam66.github.io/no-c-app/", shell=True)

if __name__ == "__main__":
    quick_fix() 