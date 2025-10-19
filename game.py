import pygame
import sys
from config import *
from snake import Snake
from food import Food

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.snake = Snake()
        self.food = Food()
        
        # Game state
        self.state = MENU
        self.score = INITIAL_SCORE
        self.speed = INITIAL_SPEED
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Ensure food doesn't spawn on snake
        self.food.respawn(self.snake.body)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == MENU:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                
                elif self.state == PLAYING:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
                    elif event.key == pygame.K_p:
                        self.state = PAUSED
                
                elif self.state == PAUSED:
                    if event.key == pygame.K_p:
                        self.state = PLAYING
                
                elif self.state == GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.restart_game()
                    elif event.key == pygame.K_ESCAPE:
                        self.state = MENU
        
        return True
    
    def update(self):
        """Update game logic"""
        if self.state == PLAYING:
            self.snake.move()
            
            # Check food collision
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 10
                self.speed += SPEED_INCREMENT
                self.food.respawn(self.snake.body)
            
            # Check game over conditions
            if self.snake.check_collision():
                self.state = GAME_OVER
    
    def draw(self):
        """Draw everything on screen"""
        self.screen.fill(BLACK)
        
        if self.state == MENU:
            self.draw_menu()
        elif self.state == PLAYING or self.state == PAUSED:
            self.draw_game()
            if self.state == PAUSED:
                self.draw_pause_overlay()
        elif self.state == GAME_OVER:
            self.draw_game()
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_menu(self):
        """Draw main menu"""
        title_text = self.font.render("SNAKE GAME", True, WHITE)
        start_text = self.small_font.render("Press SPACE to start", True, WHITE)
        quit_text = self.small_font.render("Press ESC to quit", True, WHITE)
        
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 30))
        
        self.screen.blit(title_text, title_rect)
        self.screen.blit(start_text, start_rect)
        self.screen.blit(quit_text, quit_rect)
    
    def draw_game(self):
        """Draw the game elements"""
        # Draw snake and food
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        # Draw score
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw controls
        controls_text = self.small_font.render("Arrow Keys: Move | P: Pause", True, WHITE)
        self.screen.blit(controls_text, (10, SCREEN_HEIGHT - 25))
    
    def draw_pause_overlay(self):
        """Draw pause overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font.render("PAUSED", True, WHITE)
        resume_text = self.small_font.render("Press P to resume", True, WHITE)
        
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20))
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
        
        self.screen.blit(pause_text, pause_rect)
        self.screen.blit(resume_text, resume_rect)
    
    def draw_game_over(self):
        """Draw game over overlay"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("GAME OVER", True, WHITE)
        score_text = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = self.small_font.render("Press SPACE to restart", True, WHITE)
        menu_text = self.small_font.render("Press ESC for menu", True, WHITE)
        
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 60))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
        
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(menu_text, menu_rect)
    
    def start_game(self):
        """Start a new game"""
        self.snake = Snake()
        self.food = Food()
        self.food.respawn(self.snake.body)
        self.score = INITIAL_SCORE
        self.speed = INITIAL_SPEED
        self.state = PLAYING
    
    def restart_game(self):
        """Restart the current game"""
        self.start_game()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.speed)
        
        pygame.quit()
        sys.exit()
