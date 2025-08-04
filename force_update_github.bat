@echo off
echo 🔄 Force updating GitHub Pages...
echo.

echo 📁 Adding all files...
git add .

echo 💾 Committing changes...
git commit -m "Force update: New simple website design"

echo 🚀 Pushing to GitHub...
git push

echo.
echo ✅ Update pushed to GitHub!
echo.
echo 🌐 Your website should update in 5-10 minutes at:
echo https://malam66.github.io/strong-no-recoil/
echo.
echo 🔄 If you still see the old version:
echo 1. Clear browser cache (Ctrl + Shift + Delete)
echo 2. Try incognito mode
echo 3. Wait 10-15 minutes for GitHub Pages to update
echo.
pause 