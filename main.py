import pygame
import random

# Initializing the pygame
pygame.init()

# Creating window
window = pygame.display.set_mode((1080, 800))

# FrameRate
windowFrameRate = 60

# Title and Icon
pygame.display.set_caption("Earth Defender")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Scrolling Background
background1Texture = pygame.image.load("images/background.png")
background2Texture = pygame.image.load("images/background.png")
background1Y = 0
background2Y = -2690
backgroundY_change = 1

# Player
playerTexture = pygame.image.load("images/Player1.png")
playerX = 370
playerY = 740
playerX_change = 0

# Enemy
enemyTexture = pygame.image.load("images/enemy.png")
enemyX = random.randint(0, 1034)
enemyY = random.randint(0, 50)
enemyX_change = 3
enemyY_change = 1.5


# Drawing background
def background(y1, y2):
    window.blit(background1Texture, (0, y1))
    window.blit(background2Texture, (0, y2))


def player(x, y):
    window.blit(playerTexture, (x, y))


def enemy(x, y):
    window.blit(enemyTexture, (x, y))


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

    # Background drawing
    background1Y += backgroundY_change
    background2Y += backgroundY_change
    background(background1Y, background2Y)
    if background2Y >= background2Texture.get_height():
        background2Y = -background2Texture.get_height()
    if background1Y >= background1Texture.get_height():
        background1Y = -background1Texture.get_height()



    # Player boundary
    tempPositionX = playerX + playerX_change
    if (tempPositionX > 0) and (tempPositionX < 1034):
        playerX = tempPositionX

    player(playerX, playerY)

    # Enemy boundary and Movements
    tempPositionX = enemyX + enemyX_change
    if (tempPositionX > 0) and (tempPositionX < 1034):
        enemyX = tempPositionX
        enemyY += enemyY_change
    else:
        enemyX_change *= -1

    enemy(enemyX, enemyY)

    pygame.display.update()

    # set FrameRate
    pygame.time.Clock().tick(windowFrameRate)
