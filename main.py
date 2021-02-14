import pygame

# Initializing the pygame
pygame.init()

# Creating window
window = pygame.display.set_mode((800, 600))

# FrameRate
windowFrameRate = 60


# Title and Icon
pygame.display.set_caption("Earth Defender")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Player
playerTexture = pygame.image.load("images/Player1.png")
playerX = 370
playerY = 540
playerX_change = 0


def player(x, y):
    window.blit(playerTexture, (x, y))


# Game Loop
running = True
while running:

    # RGB colors
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    tempPositionX = playerX + playerX_change
    if (tempPositionX > 0) and (tempPositionX < 736):
        playerX = tempPositionX

    player(playerX, playerY)

    pygame.display.update()

    # set FrameRate
    pygame.time.Clock().tick(windowFrameRate)
