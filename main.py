#!/usr/bin/env python3
"""
Snake Game - Main Entry Point

A classic Snake game implementation using Python and Pygame.
Controls:
- Arrow Keys: Move the snake
- P: Pause/Resume game
- SPACE: Start game or restart after game over
- ESC: Return to menu or quit

Author: AI Assistant
"""

from game import SnakeGame

def main():
    """Main function to run the Snake game"""
    print("Starting Snake Game...")
    print("Controls:")
    print("- Arrow Keys: Move the snake")
    print("- P: Pause/Resume")
    print("- SPACE: Start/Restart")
    print("- ESC: Menu/Quit")
    print()
    
    try:
        game = SnakeGame()
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure pygame is installed: pip install pygame")

if __name__ == "__main__":
    main()
