#!/usr/bin/env python3
"""
Fix Web Deployment Script
Determines the correct repository and deploys to the right URL
"""

import subprocess
import webbrowser
import time

def check_repository():
    """Check current repository and suggest fixes"""
    print("🔍 CHECKING REPOSITORY CONFIGURATION")
    print("=" * 50)
    
    # Get current repository
    result = subprocess.run("git remote get-url origin", shell=True, capture_output=True, text=True)
    current_repo = result.stdout.strip()
    
    print(f"Current repository: {current_repo}")
    print()
    
    # Available repositories
    repositories = {
        "strong-app": "https://github.com/Malam66/strong-app.git",
        "no-c-app": "https://github.com/Malam66/no-c-app.git",
        "ultimate-auto-script": "https://github.com/Malam66/ultimate-auto-script.git"
    }
    
    print("Available repositories:")
    for name, url in repositories.items():
        print(f"  • {name}: {url}")
        print(f"    Web URL: https://malam66.github.io/{name}/")
        print()
    
    return current_repo, repositories

def deploy_to_repository(repo_name, repo_url):
    """Deploy to specific repository"""
    print(f"🚀 DEPLOYING TO {repo_name.upper()}")
    print("=" * 40)
    
    # Change remote URL if needed
    subprocess.run(f'git remote set-url origin "{repo_url}"', shell=True)
    
    # Deploy
    subprocess.run("git add .", shell=True)
    subprocess.run(f'git commit -m "Deploy to {repo_name}"', shell=True)
    subprocess.run("git push origin main", shell=True)
    
    web_url = f"https://malam66.github.io/{repo_name}/"
    print(f"✅ Deployed to: {web_url}")
    
    # Open web page
    print("🌐 Opening web page...")
    webbrowser.open(web_url)
    
    return web_url

def main():
    current_repo, repositories = check_repository()
    
    print("Which repository do you want to deploy to?")
    print("1. strong-app (current)")
    print("2. no-c-app")
    print("3. ultimate-auto-script")
    print("4. Check all repositories")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        deploy_to_repository("strong-app", repositories["strong-app"])
    elif choice == "2":
        deploy_to_repository("no-c-app", repositories["no-c-app"])
    elif choice == "3":
        deploy_to_repository("ultimate-auto-script", repositories["ultimate-auto-script"])
    elif choice == "4":
        print("\n🔍 CHECKING ALL REPOSITORIES:")
        for name, url in repositories.items():
            web_url = f"https://malam66.github.io/{name}/"
            print(f"\n{name}: {web_url}")
            webbrowser.open(web_url)
            time.sleep(1)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 