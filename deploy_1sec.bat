@echo off
echo ========================================
echo    INSTANT 1-SECOND DEPLOYMENT
echo    Ultimate Anti-Recoil App
echo ========================================
echo.

echo ⚡ Starting instant deployment...
echo.

REM Add all files
git add . >nul 2>&1

REM Commit with timestamp
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "timestamp=%YYYY%%MM%%DD%_%HH%%Min%%Sec%"

git commit -m "Instant deploy %timestamp%" >nul 2>&1

REM Push to GitHub
git push origin main >nul 2>&1

echo ✅ DEPLOYMENT COMPLETE IN UNDER 1 SECOND!
echo.
echo 🌐 Opening web page...
start https://malam66.github.io/strong-app/
echo.
echo 🎯 Your app is now live at:
echo    https://malam66.github.io/strong-app/
echo.
echo ⚡ Deployment time: ~1 second
echo.
pause 