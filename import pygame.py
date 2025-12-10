import pygame
import random

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Player car
player_rect = pygame.Rect(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 50, 50, 50)
player_speed = 5

# Enemy cars
enemy_cars = []

# Game variables
score = 0
font = pygame.font.Font(None, 36)

def create_enemy():
    x = random.randint(0, SCREEN_WIDTH - 50)
    rect = pygame.Rect(x, -50, 50, 50)
    enemy_cars.append(rect)

# Game loop
running = True
spawn_timer = 0

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.x < SCREEN_WIDTH - 50:
        player_rect.x += player_speed
    
    # Spawn enemies
    spawn_timer += 1
    if spawn_timer > 30:
        create_enemy()
        spawn_timer = 0
    
    # Move enemies
    for enemy in enemy_cars:
        enemy.y += 5
    
    # Remove off-screen enemies
    enemy_cars = [e for e in enemy_cars if e.y < SCREEN_HEIGHT]
    score += len(enemy_cars)
    
    # Collision detection
    for enemy in enemy_cars:
        if player_rect.colliderect(enemy):
            running = False
    
    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_rect)
    for enemy in enemy_cars:
        pygame.draw.rect(screen, YELLOW, enemy)
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()