import pygame
from plane_sprites import *


# 初始化
pygame.mixer.init()
# 加载
pygame.mixer_music.load("/home/share/자밀킴 (Jhameel Kim) - White Lie.mp3")
# 播放
pygame.mixer.music.play()   



class PlaneGame(object):
	'''飞机大战主游戏'''
	def __init__(self)`:
		print("游戏初始化")
		# 创建游戏窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 创建游戏时钟
		self.clock = pygame.time.Clock()
		# 调用私有方法 里面的创建精灵和精灵组
		self.__create_sprites()
		# 设置定时器事件 - 每秒创建一架敌机
		pygame.time.set_timer(CREATE_ENEMT_EVENT,1000)
		# 每隔 0.5秒发射一个豆豆
		pygame.time.set_timer(HERO_FIRE_EVENT,500)

	def start_game(self):
		print("开始游戏")	

		while True:
			# 设置帧率
			self.clock.tick(60)
			# 事件监听
			self.__event_handler()
			# 碰撞检测
			self.__check_collide()
			# 更新精灵组
			self.__update_sprites()
			# 更新屏幕显示
			pygame.display.update()

	def __create_sprites(self):
		'''创建精灵和精灵组'''
		bg1 = Background("images/background.png")
		bg2 = Background("images/background.png")
		bg2.rect.y = -bg2.rect.height
		# 背景精灵组
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 敌机精灵组 
		self.enemy_group = pygame.sprite.Group()
		# 英雄精灵组
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

	def __event_handler(self):
		'''监听事件'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# 调用静态私有方法
				PlaneGame.__game_over(self.screen)

			elif event.type == CREATE_ENEMT_EVENT:
				enemy = Enemy()
				self.enemy_group.add(Enemy())

			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()

			key_pressed = pygame.key.get_pressed()
			if key_pressed[pygame.K_RIGHT]:
				print("向右移动")	
				self.hero.speed = 2
			elif key_pressed[pygame.K_LEFT]:
				self.hero.speed = -2
				print("向左移动")
			else:
				self.hero.speed = 0

	def __check_collide(self):
		'''碰撞检测'''
		# 子弹摧毁敌机
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		# 英雄撞到敌机
		self.enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)	
		# 判断列表是否有内容
		if len(self.enemies) > 0:
			# 让英雄牺牲
			
			self.hero.kill()
			PlaneGame.__game_over(self.hero)


	@staticmethod
	def __game_over(self):
		'''游戏结束了'''
		print("游戏结束")	
		pygame.quit()
		exit()

	def __update_sprites(self):
		'''更新精灵组'''
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
			# 更新精灵组里面所有精灵的位置
			group.update()
			# 绘制到屏幕上-
			group.draw(self.screen)


if __name__ == '__main__':
	# 创建游戏对象
	game = PlaneGame()
	# 调用开始游戏方法
	game.start_game()	



			    

