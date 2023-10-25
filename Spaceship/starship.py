import time

import pygame
import random

# Initialize Pygame
pygame.init()
# print(pygame.font.get_fonts())

# Set up the game window
WIDTH = 1024
HEIGHT = 768
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starship Game")

# Set up game font
game_font = pygame.font.Font(pygame.font.get_default_font(), 36)

bullets = []
# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load images
background_img = pygame.image.load("background.jpeg")
player_img = pygame.image.load("spaceship.png")
enemy_img = pygame.image.load("enemy_ship.png")
bullet_img = pygame.image.load("bullet.png")
bullet_img.fill(pygame.Color('aquamarine2'))

# Scale images
player_img = pygame.transform.scale(player_img, (44, 44))
enemy_img = pygame.transform.scale(enemy_img, (84, 84))
background_img = pygame.transform.scale(background_img, (1024, 768))
bullet_img = pygame.transform.scale(bullet_img, (10, 10))

# Set up the player
player_rect = player_img.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

# Set up the enemies
enemy_list = []
for _ in range(10):
    enemy_ship = enemy_img.get_rect()
    enemy_ship.x = random.randint(0, WIDTH - enemy_ship.width)
    enemy_ship.y = random.randint(-HEIGHT, -enemy_ship.height)
    enemy_list.append(enemy_ship)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5
    if keys[pygame.K_SPACE]:
        bullets.append([0, 0])

    # Update enemy positions
    for enemy_ship in enemy_list:
        enemy_ship.y += 2
        if enemy_ship.y > HEIGHT:
            enemy_ship.x = random.randint(0, WIDTH - enemy_ship.width)
            enemy_ship.y = random.randint(-HEIGHT, -enemy_ship.height)

        # Check for collision
        if player_rect.colliderect(enemy_ship):
            text_surface = game_font.render("GAME OVER", True, (255, 0, 0))
            window.blit(text_surface, [WIDTH // 2, HEIGHT // 2])
            pygame.display.update()
            time.sleep(2)
            running = False

    # Draw background
    window.blit(background_img, (0, 0))

    # Draw bullets
    for bullet in bullets:
        window.blit(bullet_img, pygame.Rect(bullet[0], bullet[1], 50, 50))

    # Draw player
    window.blit(player_img, player_rect)

    # Draw enemies
    for enemy_ship in enemy_list:
        window.blit(enemy_img, enemy_ship)

    # Update the game display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
