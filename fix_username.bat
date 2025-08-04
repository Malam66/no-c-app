@echo off
title Fix GitHub Username
echo Fixing GitHub Username in download.js...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://python.org
    pause
    exit /b 1
)

echo Python found
echo.
echo Running username fix script...
echo.

REM Run the fix script
python fix_username.py

pause 