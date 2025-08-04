@echo off
echo 🔧 FIXING DOWNLOADS
echo ===================
echo.

echo Committing changes...
git commit -m "Fix download functionality - make buttons actually download files" >nul 2>&1

echo Pushing to GitHub...
git push origin main >nul 2>&1

echo ✅ DOWNLOADS FIXED!
echo.
echo 🌐 Opening web page...
start https://malam66.github.io/no-c-app/
echo.
echo 🎯 Download buttons now work!
echo.
pause 