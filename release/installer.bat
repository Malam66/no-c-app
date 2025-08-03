@echo off
echo Ultimate Anti-Recoil App Installer
echo ======================================
echo.
echo Creating nice icon...
python create_nice_icon.py
echo.
echo Installing dependencies...
pip install pynput keyboard mouse
echo.
echo Building executable with nice icon...
python setup.py build
echo.
echo Creating desktop shortcut with nice icon...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Ultimate Anti-Recoil App.lnk'); $Shortcut.TargetPath = '%~dp0build\\exe.win-amd64-3.11\\UltimateAntiRecoilApp.exe'; $Shortcut.WorkingDirectory = '%~dp0build\\exe.win-amd64-3.11'; $Shortcut.Description = 'Ultimate Anti-Recoil App'; $Shortcut.IconLocation = '%~dp0build\\exe.win-amd64-3.11\\UltimateAntiRecoilApp.exe,0'; $Shortcut.Save()"
echo.
echo Installation complete!
echo Desktop shortcut created: "Ultimate Anti-Recoil App"
echo The app now has a nice shield icon with crosshair!
echo You can now run the app from your desktop!
echo.
pause
