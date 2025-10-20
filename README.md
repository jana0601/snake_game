# Snake Game - Windows Application

A classic Snake game implementation using Python and Pygame, packaged as a Windows executable.
---
## Interface

![Snake Game Interface](https://github.com/jana0601/snake_game/blob/main/interface.jpg?raw=true)

---
## Features

- Classic Snake gameplay mechanics
- Smooth movement and collision detection
- Score tracking
- Pause functionality
- Game over screen with restart option
- Clean, modern interface
- **Standalone Windows executable** - No Python installation required!
---
## Requirements

### For Development:
- Python 3.6 or higher
- Pygame 2.5.0 or higher
- PyInstaller 5.0.0 or higher

### For Running the Game:
- Windows 7 or higher
- No additional software required!
---
## Quick Start (Windows Executable)

1. Download `SnakeGame.exe` from the `dist` folder
2. Double-click to run the game
3. Enjoy playing Snake!
---
## Development Setup

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---
## Building Windows Executable

### Method 1: Using Batch Script (Windows)
```bash
build_windows_app.bat
```

### Method 2: Using Shell Script (Linux/Mac)
```bash
chmod +x build_windows_app.sh
./build_windows_app.sh
```

### Method 3: Manual Build
```bash
pip install pyinstaller
pyinstaller snake_game.spec
```
---
## Running from Source

```bash
python main.py
```
---
## Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **P**: Pause/Resume the game
- **SPACE**: Start a new game or restart after game over
- **ESC**: Return to main menu or quit the game
---
## Game Rules

1. Control the snake to eat the red food
2. Each food eaten increases your score by 10 points
3. The snake grows longer with each food consumed
4. Avoid hitting the walls or the snake's own body
5. The game speed increases as your score grows
---
## Project Structure

```
snake_game/
├── main.py                  # Main entry point
├── game.py                  # Game state management and main loop
├── snake.py                 # Snake class and logic
├── food.py                  # Food class and generation
├── config.py                # Game configuration and constants
├── snake_game.spec          # PyInstaller configuration
├── build_windows_app.bat    # Windows build script
├── build_windows_app.sh     # Linux/Mac build script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```
---
## Distribution

The built executable (`SnakeGame.exe`) can be distributed to any Windows computer without requiring Python or any additional software to be installed.

### File Size Optimization

The executable includes all necessary Python libraries and pygame assets. Typical file size is around 15-25 MB.
---
## Customization

You can modify the game settings in `config.py`:
- Screen dimensions
- Grid size
- Colors
- Game speed
- Score increments
---
## Troubleshooting

### Build Issues
- Ensure Python 3.6+ is installed
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Try running `pyinstaller --clean snake_game.spec` to clean build cache

### Runtime Issues
- If the game doesn't start, try running from command line to see error messages
- Ensure Windows Defender or antivirus isn't blocking the executable
- Try running as administrator if permission issues occur
---
## Future Enhancements

- High score persistence
- Sound effects
- Different difficulty levels
- Power-ups
- Multiplayer mode
- Mobile touch controls
- Custom themes
---
## License

This project is open source and available under the MIT License.
