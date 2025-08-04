@echo off
echo 🚀 Deploying Ultimate Gaming App to GitHub...
echo.

echo 📦 Creating deployment files...
python deploy_to_github.py
echo.

echo 🌐 Creating web files...
python deploy_web.py
echo.

echo 🔧 Initializing Git repository...
if not exist .git (
    git init
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

echo 📝 Adding files to Git...
git add .
echo ✅ Files added to Git

echo 💾 Committing changes...
git commit -m "Deploy Ultimate Gaming App - $(date /t)"
echo ✅ Changes committed

echo 🚀 Pushing to GitHub...
git push origin main
echo ✅ Pushed to GitHub

echo.
echo ✅ GitHub deployment complete!
echo 📁 Check your repository at: https://github.com/YOUR_USERNAME/ultimate-gaming-app
echo 🌐 Web page will be at: https://YOUR_USERNAME.github.io/ultimate-gaming-app
echo.
echo 📋 Next steps:
echo 1. Create repository on GitHub if not done yet
echo 2. Enable GitHub Pages in repository settings
echo 3. Update repository URL in README.md
echo.

pause 