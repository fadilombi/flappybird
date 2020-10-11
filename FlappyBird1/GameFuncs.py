import pygame
import random
import sys
from vars import WIDTH, HEIGHT, YELLOW, game_font

def menu(screen, bg_surface1, main, droppingValue, bird_dropping, score, pipes, birds):
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					main(droppingValue, bird_dropping, score, pipes, birds)
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()

		screen.blit(bg_surface1, (0, 0))

		pygame.display.update()

def game_over(screen, game_overS, bg_surface1, main, droppingValue, bird_dropping, score, pipes, birds):
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
				if event.key == pygame.K_SPACE:
					birds.empty()
					pipes.empty()
					score = 0
					bird_dropping = 0
					main(droppingValue, bird_dropping, score, pipes, birds)


		screen.blit(game_overS, (0, 0))

		pygame.display.update()

	


def floor_top_collision(bird, floor_rect, floor2_rect, screen, game_overS, bg_surface1, main, droppingValue, bird_dropping, pipes, score, birds):
	if bird.rect.top <= 0:
		game_over(screen, game_overS, bg_surface1, main, droppingValue, bird_dropping, score, pipes, birds)
	if bird.rect.bottom >= floor_rect.top or bird.rect.bottom >= floor2_rect.top:
		game_over(screen, game_overS, bg_surface1, main, droppingValue, bird_dropping, score, pipes, birds)

	

def moving_floor(floor2_rect, floor_rect, FLOOR1_POS, FLOOR2_POS):
	if floor2_rect.centerx == FLOOR1_POS[0]:
		floor_rect.centerx = FLOOR2_POS[0]
	if floor_rect.centerx == FLOOR1_POS[0]:
		floor2_rect.centerx = FLOOR2_POS[0]

def show_score(WIDTH, HEIGHT, YELLOW, screen, game_font, score):
	score_surface = game_font.render(str(int(score)), True, YELLOW)
	score_rect = score_surface.get_rect(center = (WIDTH // 2, HEIGHT // 4 - 50))
	screen.blit(score_surface, score_rect)










