import pygame


class GameSprite(pygame.sprite.Sprite):
	
	def __init__(self.imagae_name,speed=1):
		super().__init__()

self.image = pygame.image.load(imagae_name)		
self.rect = self.image.get_rect()
self.speed = speed

	def update(self,*args):
		super().__init__()

self.rect.y += self.speed		