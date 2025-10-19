import random
import pygame
from config import GRID_WIDTH, GRID_HEIGHT, RED, GRID_SIZE, WHITE

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.color = RED
        
    def generate_position(self):
        """Generate a random position for food that doesn't overlap with snake"""
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)
    
    def respawn(self, snake_body):
        """Respawn food at a new position that doesn't overlap with snake"""
        while True:
            self.position = self.generate_position()
            if self.position not in snake_body:
                break
    
    def draw(self, screen):
        """Draw the food on the screen"""
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, WHITE, rect, 1)  # Border
