import pygame
from pygame.sprite import Sprite


# pipe class
class Pipe(Sprite):
	def __init__(self, screen, x, y): # initialize pipe class
		super(Pipe, self).__init__() # initialize sprite class
		self.screen = screen
		self.x = x
		self.y = y



		self.pipe_up_img = pygame.image.load('images/pipe1.png').convert()
		self.rect = self.pipe_up_img.get_rect(center = (self.x, self.y))


	# blit method
	def blitme(self):
		self.screen.blit(self.pipe_up_img, self.rect)

class Pipe_down(Sprite):
	def __init__(self, screen, x, y): # initialize pipe class
		super(Pipe_down, self).__init__() # initialize sprite class
		self.screen = screen
		self.x = x
		self.y = y

		self.pipe_down_img = pygame.image.load('images/pipe.png').convert()
		self.rect = self.pipe_down_img.get_rect(center = (self.x, self.y))

	# blit method
	def blitme(self):
		self.screen.blit(self.pipe_down_img, self.rect)



		
