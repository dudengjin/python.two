import pygame
from plane_sprites import *

# pygame.time.set_timer(CREATE_ENEMY_EVENY,1000)

# HERO_FIRE_EVEENT = pygame.USEREVENT + 1

class PlaneGame(object):
	'''飞机大战主游戏类'''

	def __init__(self):
		print("游戏初始化")		

		
		# 创建游戏窗口
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		# 创建游戏时钟
		self.clock = pygame.time.Clock()
		# 调用私有方法，精灵和精灵组的创建
		self.__create_sprites()

		# pygame.time.set_timer(HERO_FIRE_EVEENT,500)

	def start_game(self):
		print("游戏开始")		

		while True:

			self.clock.tick(60)  # 设置刷新帧率
			self.__event_handler()  # 事件监听
			self.__check_collide()  # 碰撞检测
			self._update_sprites()  # 更新精灵组
			pygame.display.update()  # 更新屏幕显示

	def __create_sprites(self):
		
		self.back_group = pygame.sprite.Group()
		self.enemy_group = pygame.sprite.Group()
		self.hero_group = pygame.sprite.Group()

		'''
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
		self.enemy_group = pygame.sprite.Group()

		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
		'''	

	def __event_handler(self):
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				PlaneGame._game_over()
			
			pygame.quit()		
			exit()

	@staticmethod
	def __game_over():
		print("游戏结束")
			
		'''
		elif event.type == CREATE_ENEMY_EVENY:
			print("敌机出场....")

		elif event.type == CREATE_ENEMY_EVENY:
			self.enemy_group.add(Enemy())

		elif event.type == HERO_FIRE_EVEENT:
			self.hero.fire()	
		'''	

	def __check_collide(self):
		pass
		'''
		self.black_group = pygame.sprite.Group()
		self.enemy_group = pygame.sprite.Group()
		self.hero_group = pygame.sprite.Group()

		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		
		if len(enemies) > 0:
			self.hero.kill()
		'''

	def __update_sprites(self):
		
		
		for group in [self.black_group,self.enemy_group,self.hero_group]:
			
			group.update
			group.draw(self.screen)
			'''
			self.back_group.update()
			group.back_group.draw(self.screen)
	
			self.enemy_group.update()
			self.enemy_group.draw(self.screen)

			self.hero_group.update()
			self.hero_group.draw(self.screen)
			'''

	def __create_sprites(self):
		pass
		'''
		bg1 = Background("./images/background.png")
		bg2 = Background("./images/background.png")
		bg2.rect.y = -bg2.rect.height

		self.black_group = pygame.sprite.Group(bg1,bg2)
		'''

if __name__ == '__main__':
	 
	 game = PlaneGame()
	 game.start_game()

