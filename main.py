import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load("background.png")
pygame.display.set_caption("spaceinvaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
playerimg = pygame.image.load("player.png")
playerx = PLAYER_START_X
playery = PLAYER_START_Y
playerx_change = 0
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0,SCREEN_WIDTH - 64))
    enemyy.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyx_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_Y)
bulletimg = pygame.image.load("bullet.png")
bulletx = 0
bullety = PLAYER_START_Y
bulletx_change = 0
bullety_change = BULLET_SPEED_Y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textx = 10
texty = 10
over_font = pygame.font.Font("freesansbold.ttf",64)