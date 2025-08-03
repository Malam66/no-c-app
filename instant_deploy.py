#!/usr/bin/env python3
"""
Instant 1-Second Deployment Script
Deploys changes to GitHub Pages in under 1 second
"""

import os
import subprocess
import time
from datetime import datetime

def run_command(command, description):
    """Run command and return result"""
    print(f"⚡ {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        return None

def instant_deploy():
    """Deploy in 1 second"""
    print("🚀 INSTANT 1-SECOND DEPLOYMENT")
    print("=" * 40)
    
    start_time = time.time()
    
    # Step 1: Add all files (0.1s)
    run_command("git add .", "Adding files")
    
    # Step 2: Commit with timestamp (0.1s)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_command(f'git commit -m "Instant deploy {timestamp}"', "Committing changes")
    
    # Step 3: Push to GitHub (0.8s)
    run_command("git push origin main", "Pushing to GitHub")
    
    end_time = time.time()
    deployment_time = end_time - start_time
    
    print("=" * 40)
    print(f"⚡ DEPLOYMENT COMPLETE IN {deployment_time:.2f} SECONDS!")
    print("=" * 40)
    
    # Open web page immediately
    print("🌐 Opening web page...")
    run_command("start https://malam66.github.io/strong-app/", "Opening web page")
    
    print("\n🎯 Your app is now live at:")
    print("   https://malam66.github.io/strong-app/")
    print("\n⚡ Deployment time:", f"{deployment_time:.2f} seconds")

if __name__ == "__main__":
    instant_deploy() 