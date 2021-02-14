import pygame
import random
import math

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

score = 0

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

# Projectile
projectileTexture = pygame.image.load("images/projectile.png")
projectileX = playerX
projectileY = playerY
projectileY_change = -10
projectile_state = "ready"


# Drawing background
def background(y1, y2):
    window.blit(background1Texture, (0, y1))
    window.blit(background2Texture, (0, y2))


def player(x, y):
    window.blit(playerTexture, (x, y))


def enemy(x, y):
    window.blit(enemyTexture, (x, y))


def fire_projectile(x, y):
    global projectile_state
    projectile_state = "fire"
    window.blit(projectileTexture, (x + 25.5, y + 10))


def is_collision(enemy_x, enemy_y, projectile_x, projectile_y):
    distance = math.sqrt(math.pow(enemy_x - projectile_x, 2) + math.pow(enemy_y - projectile_y, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB colors
    window.fill((0, 0, 0))

    # Background drawing
    background1Y += backgroundY_change
    background2Y += backgroundY_change
    background(background1Y, background2Y)
    if background2Y >= background2Texture.get_height():
        background2Y = -background2Texture.get_height()
    if background1Y >= background1Texture.get_height():
        background1Y = -background1Texture.get_height()

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
            if event.key == pygame.K_SPACE:
                projectile_state = "fire"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Projectile movements
    if projectileY < 0:
        projectile_state = "ready"
        projectileY = playerY
    if projectile_state == "ready":
        projectileX = playerX
        projectileY = playerY
    if projectile_state == "fire":
        fire_projectile(projectileX, projectileY)
        projectileY += projectileY_change

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

    # Collision checking
    collision = is_collision(enemyX, enemyY, projectileX, projectileY)
    if collision:
        projectile_state = "ready"
        score += 1
        print(score)

    pygame.display.update()

    # set FrameRate
    pygame.time.Clock().tick(windowFrameRate)
