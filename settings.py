import pygame

vec = pygame.math.Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (186, 55, 5)

WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Doggo tilemap demo"
BGCOLOR = BROWN

TILESIZE = 32
GRIDWITH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tile_01.png'

#Player settings
PLAYER_SPEED = 250
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

#Gun
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 3

#Mobs
MOB_IMG = 'zoimbie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pygame.Rect(0, 0, 30, 30)