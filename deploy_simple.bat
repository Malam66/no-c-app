@echo off
echo 🔧 DEPLOYING SIMPLE WEB PAGE
echo =============================
echo.

echo Committing changes...
git commit -m "Simplify web page - show only download functionality" >nul 2>&1

echo Pushing to GitHub...
git push origin main >nul 2>&1

echo ✅ SIMPLE WEB PAGE DEPLOYED!
echo.
echo 🌐 Opening web page...
start https://malam66.github.io/no-c-app/
echo.
echo 🎯 Web page now shows only download buttons!
echo.
pause 