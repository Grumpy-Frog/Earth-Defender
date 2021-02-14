import pygame

# Initializing the pygame
pygame.init()

# Creating window
window = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Earth Defender")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Player
playerTexture = pygame.image.load("images/Player1.png")
playerX = 370
playerY = 480


def player():
    window.blit(playerTexture, (playerX, playerY))


# Game Loop
running = True
while running:

    # RGB colors
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()
