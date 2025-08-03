#!/usr/bin/env python3
"""
Deploy Ultimate Anti-Recoil App to malam66 GitHub account
"""

import os
import subprocess
import shutil

def run_git_command(command, description):
    """Run git command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None

def deploy_to_malam66():
    """Deploy the app to malam66 GitHub account"""
    print("🚀 Deploying Ultimate Anti-Recoil App to malam66 GitHub...")
    print("=" * 60)
    
    # Step 1: Initialize git if not already done
    if not os.path.exists(".git"):
        run_git_command("git init", "Initializing git repository")
    
    # Step 2: Add all files
    run_git_command("git add .", "Adding all files to git")
    
    # Step 3: Create initial commit
    run_git_command('git commit -m "Ultimate Anti-Recoil App v2.0.0 - Professional Windows app with GUI and desktop integration"', "Creating initial commit")
    
    # Step 4: Add remote repository (malam66)
    run_git_command("git remote add origin https://github.com/malam66/ultimate-anti-recoil-app.git", "Adding malam66 remote repository")
    
    # Step 5: Push to main branch
    run_git_command("git push -u origin main", "Pushing to main branch")
    
    # Step 6: Create and push version tag
    run_git_command('git tag -a v2.0.0 -m "Release v2.0.0 - Ultimate Anti-Recoil App"', "Creating version tag")
    run_git_command("git push origin v2.0.0", "Pushing version tag")
    
    print("\n🎉 Deployment to malam66 GitHub completed!")
    print("=" * 60)
    print("📋 Your app is now available at:")
    print("🌐 Repository: https://github.com/malam66/ultimate-anti-recoil-app")
    print("🌐 Web Page: https://malam66.github.io/ultimate-anti-recoil-app/")
    print("📦 Releases: https://github.com/malam66/ultimate-anti-recoil-app/releases")
    print("\n📝 Next steps:")
    print("1. Go to https://github.com/malam66/ultimate-anti-recoil-app")
    print("2. Enable GitHub Pages: Settings → Pages → Source: Deploy from branch → main → /docs")
    print("3. Enable GitHub Actions: Settings → Actions → General → Allow all actions")
    print("4. Test the web installer at: https://malam66.github.io/ultimate-anti-recoil-app/")

if __name__ == "__main__":
    deploy_to_malam66() 