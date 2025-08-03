#!/usr/bin/env python3
"""
Quick Web Fix - Deploy to no-c-app repository
"""

import subprocess
import webbrowser

def fix_web():
    print("🔧 FIXING WEB DEPLOYMENT")
    print("=" * 30)
    
    # Set repository to no-c-app
    print("Setting repository to no-c-app...")
    subprocess.run("git remote set-url origin https://github.com/Malam66/no-c-app.git", shell=True)
    
    # Add all files
    print("Adding files...")
    subprocess.run("git add .", shell=True)
    
    # Commit
    print("Committing changes...")
    subprocess.run('git commit -m "Fix web deployment"', shell=True)
    
    # Push
    print("Pushing to GitHub...")
    subprocess.run("git push origin main", shell=True)
    
    # Open web page
    web_url = "https://malam66.github.io/no-c-app/"
    print(f"✅ Deployed to: {web_url}")
    print("Opening web page...")
    webbrowser.open(web_url)
    
    print("\n🎯 Web should now be working!")
    print(f"URL: {web_url}")

if __name__ == "__main__":
    fix_web() 