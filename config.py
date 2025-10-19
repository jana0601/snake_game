# Game Configuration Constants

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game grid settings
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 200, 0)
GRAY = (128, 128, 128)

# Game settings
INITIAL_SPEED = 10
SPEED_INCREMENT = 1
INITIAL_SCORE = 0

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
PAUSED = 3
