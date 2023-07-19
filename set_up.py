import pygame, sys, random
import os

# Set up the game
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 900, 500
SURFACE_HEIGHT = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maple Story")

WHITE = (255, 255, 255); BLACK = (0, 0, 0);RED = (255, 0, 0); GREEN =((0,230,0))
YELLOW = (255, 255, 0);BLUE_NAVY = (12, 45, 72);BLUE = (8,0,255)

BORDER = pygame.draw.line(WIN, BLACK, (0, SURFACE_HEIGHT), (WIDTH, SURFACE_HEIGHT), 5)
HEALTH_FONT = pygame.font.SysFont('comicsans', 25)
ENEMY_HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
ENEMY_HIT = pygame.USEREVENT + 3
bullets = []
BULLET_SPEED = 100

MAX_UNIVERSE =5
COUNT_UNIVERSE = 1
FPS = 60
VELOCITY =5
BULLET_VEL = 7
MAX_BULLETS = 3
PLAYER_WIDTH, PLAYER_HEIGHT = 80, 72

IS_JUMPING = False
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'story_image1.png')), (WIDTH, HEIGHT))
