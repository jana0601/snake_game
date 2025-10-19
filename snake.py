import pygame
from config import GRID_WIDTH, GRID_HEIGHT, GREEN, DARK_GREEN, GRID_SIZE, UP, DOWN, LEFT, RIGHT, WHITE

class Snake:
    def __init__(self):
        # Start snake in the middle of the screen
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = [(start_x, start_y)]
        self.direction = RIGHT
        self.grow_pending = False
        
    def move(self):
        """Move the snake in the current direction"""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
    
    def change_direction(self, new_direction):
        """Change snake direction (prevent moving backwards)"""
        # Prevent moving in opposite direction
        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
            self.direction = new_direction
    
    def grow(self):
        """Mark snake to grow on next move"""
        self.grow_pending = True
    
    def check_collision(self):
        """Check if snake collides with walls or itself"""
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if (head_x < 0 or head_x >= GRID_WIDTH or 
            head_y < 0 or head_y >= GRID_HEIGHT):
            return True
        
        # Check self collision
        if self.body[0] in self.body[1:]:
            return True
        
        return False
    
    def draw(self, screen):
        """Draw the snake on the screen"""
        for i, segment in enumerate(self.body):
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            
            # Head is darker green
            color = DARK_GREEN if i == 0 else GREEN
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)  # Border
