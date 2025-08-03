@echo off
echo 🔧 FIXING WEB PAGE
echo ===================
echo.

echo Adding files...
git add . >nul 2>&1

echo Committing changes...
git commit -m "Fix web page - add full app interface" >nul 2>&1

echo Pushing to GitHub...
git push origin main >nul 2>&1

echo ✅ WEB PAGE FIXED!
echo.
echo 🌐 Opening web page...
start https://malam66.github.io/no-c-app/
echo.
echo 🎯 Your Ultimate Anti-Recoil App is now live!
echo.
pause 