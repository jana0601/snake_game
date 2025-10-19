@echo off
echo Building Snake Game Windows Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6+ and try again
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not available
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

echo Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo Error: Failed to install required packages
    pause
    exit /b 1
)

echo.
echo Building executable...
pyinstaller snake_game.spec

if errorlevel 1 (
    echo Error: Failed to build executable
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo.
echo The executable can be found in: dist\SnakeGame.exe
echo.
echo You can now distribute SnakeGame.exe to other Windows computers
echo without requiring Python to be installed.
echo.
pause
