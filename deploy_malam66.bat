@echo off
echo ========================================
echo    Deploying to malam66 GitHub
echo    Ultimate Anti-Recoil App
echo ========================================
echo.

echo Step 1: Preparing deployment files...
python deploy_to_github.py
echo.

echo Step 2: Deploying to malam66 GitHub...
python deploy_to_malam66.py
echo.

echo ========================================
echo    DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo Your app is now available at:
echo.
echo Repository: https://github.com/malam66/ultimate-anti-recoil-app
echo Web Page:   https://malam66.github.io/ultimate-anti-recoil-app/
echo Releases:   https://github.com/malam66/ultimate-anti-recoil-app/releases
echo.
echo Next steps:
echo 1. Go to the repository URL above
echo 2. Enable GitHub Pages (Settings > Pages > Deploy from branch > main > /docs)
echo 3. Enable GitHub Actions (Settings > Actions > General > Allow all actions)
echo 4. Test the web installer
echo.
echo ========================================
pause 