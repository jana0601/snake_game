@echo off
echo Building Snake Game Windows Application...
echo.

REM Install PyInstaller if not already installed
pip install pyinstaller

REM Build the executable
echo Building executable...
pyinstaller --onefile --console --name SnakeGame main.py

REM Check if build was successful
if exist "dist\SnakeGame.exe" (
    echo.
    echo Build completed successfully!
    echo The executable can be found at: dist\SnakeGame.exe
    echo.
    echo File size:
    dir dist\SnakeGame.exe
    echo.
    echo You can now run the game by double-clicking SnakeGame.exe
) else (
    echo.
    echo Build failed. Please check the error messages above.
)

echo.
pause
