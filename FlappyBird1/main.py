#importing libraries
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
import sys
import random 
import GameFuncs as gf
from bird import Bird
from pipe import Pipe, Pipe_down
from vars import WIDTH, HEIGHT, FLOOR_WIDTH, FLOOR_HEIGHT, FLOOR1_POS, FLOOR2_POS, BLUE, YELLOW
from vars import pipes_x_pos, droppingValue, bird_dropping, score, run, pipe_moving_speed, FPS, spawn_time, game_font

# initialize pygame
pygame.init()

# calling clock class
clock = pygame.time.Clock()

#setting screen and screen caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Flappy Bird")

# background Image
bg_surface = pygame.image.load('images/background-day.png').convert()
bg_surface = pygame.transform.scale(bg_surface, (WIDTH, HEIGHT))

# menu background
bg_surface1 = pygame.image.load('images/background-day1.png').convert()
bg_surface1 = pygame.transform.scale(bg_surface1, (WIDTH, HEIGHT))


# game over screen 
game_overS = pygame.image.load('images/gameoverscreen.png').convert()
game_overS = pygame.transform.scale(game_overS, (WIDTH, HEIGHT))

# floor surface
floor_surface = pygame.image.load('images/base.png')
floor_surface = pygame.transform.scale(floor_surface, (FLOOR_WIDTH, FLOOR_HEIGHT))
floor_rect = floor_surface.get_rect(center = (FLOOR1_POS))

floor2_surface = pygame.image.load('images/base.png')
floor2_surface = pygame.transform.scale(floor_surface, (FLOOR_WIDTH, FLOOR_HEIGHT))
floor2_rect = floor_surface.get_rect(center = (FLOOR2_POS))



# group that contains pipes
pipes = Group()
birds = Group()

# pipes spawn
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, spawn_time)

# main function
def main(droppingValue, bird_dropping, score, pipes, birds):
	from vars import pipe_moving_speed
	# make New Pipe
	def new_pipe():
		x = random.randint(WIDTH // 2 + 50, WIDTH + 50)
		new_pipe = Pipe(screen, x, random.randint(0, HEIGHT // 2 - 300))
		new_down_pipe = Pipe_down(screen, x, random.randint(HEIGHT // 2 + 100, HEIGHT))
		pipes.add(new_pipe)
		pipes.add(new_down_pipe)

	def collision():
		collisions = pygame.sprite.groupcollide(birds, pipes, True, False)

	bird1 = Bird(screen, WIDTH // 2, HEIGHT // 3)
	birds.add(bird1)

	new_pipe()

	# game loop
	while True:
		clock.tick(FPS) # Frames Per Second
		# event for loop
		for event in pygame.event.get():
			# check if quit == True
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				# binding keys
			if event.type == pygame.KEYDOWN:
				# jumping key
				if event.key == pygame.K_SPACE:
					bird1.bird_surface = pygame.image.load('images/birdup.png').convert()
					bird_dropping = 1
					bird_dropping *= -4
					# QUIT key
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					bird1.bird_surface = pygame.image.load('images/midbird.png').convert()

			if event.type == SPAWNPIPE:
				new_pipe()

		#if birds.sprites()[0].rect.centerx > pipes.sprites()[0].rect.centerx or birds.sprites()[0].rect.centerx > pipes.sprites()[1].rect.centerx:
		#	score += 1




		
		# check for floor collisions
		gf.floor_top_collision(bird1, floor_rect, floor2_rect, screen, game_overS, bg_surface1, main, droppingValue, bird_dropping, pipes, score, birds)

		
		# moving the floor function
		gf.moving_floor(floor2_rect, floor_rect, FLOOR1_POS, FLOOR2_POS)
		if bird_dropping >= 3:
			bird1.bird_surface = pygame.image.load('images/birddown.png').convert()

		# displaying the background			
		screen.blit(bg_surface, (0, 0))
		bird_dropping += droppingValue
		bird1.rect.centery += bird_dropping
		floor_rect.centerx -= 1 
		floor2_rect.centerx -= 1

		# moving pipes
		for pipe in pipes.sprites():
			pipe.blitme()
			pipe.rect.centerx -= pipe_moving_speed
			if pipe.rect.right <= 0:
				pipes.remove(pipe)
				score += 0.5



		if not birds:
			gf.game_over(screen, game_overS, bg_surface1, main, droppingValue, bird_dropping, score, pipes, birds)

		# displaying floor
		screen.blit(floor_surface, floor_rect)
		screen.blit(floor2_surface, floor2_rect)

		# displaying bird
		for bird in birds.sprites():
			bird.blitme()

		# displaying score 
		gf.show_score(WIDTH, HEIGHT, YELLOW, screen, game_font, score)

		collision()

		# updating the display
		pygame.display.update()

#call menu function
gf.menu(screen, bg_surface1, main, droppingValue, bird_dropping, score, pipes, birds)