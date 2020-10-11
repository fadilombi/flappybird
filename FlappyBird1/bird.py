import pygame
from pygame.sprite import Sprite


# bird Class
class Bird(Sprite):
	"""docstring for Bird"""
	def __init__(self, screen, x, y):
		super(Bird, self).__init__()
		self.screen = screen
		self.x = x
		self.y = y

		self.bird_surface = pygame.image.load('images/midbird.png').convert()
		self.rect = self.bird_surface.get_rect(center = (self.x, self.y))

	def blitme(self):
		self.screen.blit(self.bird_surface, self.rect)