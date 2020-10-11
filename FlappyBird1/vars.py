import pygame
import random


pygame.font.init()

WIDTH = 360
HEIGHT = 640

FLOOR_WIDTH = 400
FLOOR_HEIGHT = 112

FLOOR1_POS = 180, 620
FLOOR2_POS = FLOOR1_POS[0] + 400, FLOOR1_POS[1]

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Flappy Bird")

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pipes_x_pos = random.randint(WIDTH // 2 + 50, WIDTH)

droppingValue = 0.25
bird_dropping = 0

score = 0

run = True

FPS = 60

pipe_moving_speed = 1.3

spawn_time = random.randint(1200, 2200)

# FONT
game_font = pygame.font.Font('04B_19__.TTF', 55)

