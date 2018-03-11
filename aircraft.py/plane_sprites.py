import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# CREATE_ENEMY_EVENY = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):

	def __init__(self,image_url,new_speed=1):
		
		super().__init__()
		self.image = pygame.image.load(image_url)
		self.rect = self.image.get_rect()
		self.speed = new_speed

		
	# def update(self):
		# super().update()

		# if self.rect.y >= SCREEN_RECT.height:
			# self.rect.y = self.rect.height

'''
class Enemy(GameSprite):
	
	def __init__(self):
		super().__init__("./images/enemy1.png")

	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			print("敌机飞出屏幕...")

import random

def __init__(self):
	super().__init__("./images/enemy1.png")

	self.speed = random.randint(1, 3)
	self.rect.bottom = 0
	max.x = SCREEN_RECT.width - self.rect.width
	self.rect.x = random.randint(0, man_x)

	def __del__(self):
		print("敌机挂了%s"%self.rect)

 
	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
'''
'''
class Hero(GameSprite):
	
	def __init__(self):
		super().__init__("./images/me1.png",0)

		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

		self.bullets = pygaem.sprite.Group()

	def update(self):
		
		self.rect.x += self.speed

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right	

keys_pressed = pygame.key.get_pressed()	

if keys_pressed[pygame.K_RIGHT]:
	
	self.hero.speed = 2
elif keys_pressed[pygame.K_LEFT]:

	self.hero.speed = -2
else:

	self.hero.speed = 0			

	def fire(self):
		print("发射子弹...")

		for i in (1,2,3,):

			bullet = Bullet()

			bullet.rect.bottom = self.rect.y - 20
			bullet.rect.centerx = self.rect.centerx

			self.bullet.add(bullet)
'''
'''
class Bullet(GameSprite):
	
	def __init__(self):
		super().__init__("./images/bullet1.png",-2)

	def update(self):
		super().update()

		if self.rect.bottom < 0:
			self.kill()
'''

