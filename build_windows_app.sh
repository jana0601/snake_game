#!/bin/bash

echo "Building Snake Game Windows Application..."
echo

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed or not in PATH"
    echo "Please install Python 3.6+ and try again"
    exit 1
fi

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "Error: pip is not available"
    echo "Please ensure pip is installed with Python"
    exit 1
fi

echo "Installing required packages..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "Error: Failed to install required packages"
    exit 1
fi

echo
echo "Building executable..."
pyinstaller snake_game.spec

if [ $? -ne 0 ]; then
    echo "Error: Failed to build executable"
    exit 1
fi

echo
echo "Build completed successfully!"
echo
echo "The executable can be found in: dist/SnakeGame.exe"
echo
echo "You can now distribute SnakeGame.exe to other Windows computers"
echo "without requiring Python to be installed."
echo
