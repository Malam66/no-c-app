@echo off
echo 🚀 ULTIMATE GAMING APP - 1 SECOND DEPLOYMENT
echo.

echo ⚡ Quick deployment starting...
python deploy_to_github.py
python deploy_web.py
git add .
git commit -m "Ultimate Gaming App - Quick Update"
git push origin main

echo.
echo ✅ DEPLOYMENT COMPLETE IN 1 SECOND!
echo 📁 Repository: https://github.com/Malam66/no-c-app
echo 🌐 GitHub Pages: https://malam66.github.io/no-c-app/
echo. 