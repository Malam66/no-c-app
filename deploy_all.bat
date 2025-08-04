@echo off
echo 🚀 Deploying Ultimate Gaming App to GitHub and Web...
echo.

echo 📦 Creating deployment files...
python deploy_to_github.py
echo.

echo 🌐 Creating web files...
python deploy_web.py
echo.

echo ✅ Deployment complete!
echo 📁 Check the 'release' and 'web' directories
echo 🌐 Upload web/index.html to your web hosting
echo 📂 Upload release/ files to GitHub
echo.

pause 