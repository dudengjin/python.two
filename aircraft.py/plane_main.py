import pygame
from plane_sprites import *

# 初始化
pygame.mixer.init()
# 加载
pygame.mixer_music.load("/home/share/许嵩 - 雅俗共赏.mp3")
# 播放
pygame.mixer.music.play()   



class PlaneGame(object):
	'''飞机大战主游戏类'''

	def __init__(self):
		print("游戏初始化")		

		# 创建游戏窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		# 创建游戏时钟
		self.clock = pygame.time.Clock()
		# 调用私有方法，精灵和精灵组的创建
		self.__create_sprites()

		# 定时器事件,每秒钟创建一架敌机
		pygame.time.set_timer(CREATE_ENEMT_EVENT,1000)
		# 设置定时器,每隔多少秒,创建一个敌机
		pygame.time.set_timer(HERO_FIRE_EVENT,500)

	def start_game(self):
		print("游戏开始")		

		while True:
			# 设置刷新帧率
			self.clock.tick(60)  
			# 事件监听
			self.__event_handler()  
			# 碰撞检测
			self.__check_collide() 
			# 更新精灵组
			self.__update_sprites() 
			# 更新屏幕显示
			pygame.display.update()  



	def __event_handler(self):
		'''事件监听'''
		for event in pygame.event.get():
			# print(event)
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMT_EVENT:
				print("敌机出场")	
				self.enemy_group.add(Enemy())
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()


		keys_pressed = pygame.key.get_pressed()	
		
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 2
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -2
		else:
			self.hero.speed = 0		
		'''
		elif keys_pressed[pygame.K_UP]:
			
		elif keys_pressed[pygame.K_DOWN]:
		'''	
		

	def __check_collide(self):
		'''碰撞检测'''
		
		# 子弹摧毁飞机
		pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		# 敌机撞毁飞机
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		# 判断列表是否有内容
		if len(enemies) > 0:
			# 让英雄牺牲
			self.hero.kill()
			PlaneGame.__game_over()

	@staticmethod
	def __game_over():
		'''游戏结束'''
		print("游戏结束")
		
		# 卸载模块
		pygame.quit()
		# 退出python脚本
		exit()
			
	def __create_sprites(self):
		'''创建精灵和精灵组'''
		bg1 = BackGround()
		bg2 = BackGround(True)
		bg2.rect.y = -bg2.rect.height
		
		self.hero = Hero()
		# 背景组
		self.back_group = pygame.sprite.Group(bg1,bg2)
		# 敌机组
		self.enemy_group = pygame.sprite.Group()
		# 英雄组
		self.hero_group = pygame.sprite.Group(self.hero)
		# 子弹组
		self.bullets = pygame.sprite.Group()


	def __update_sprites(self):
		'''更新精灵和精灵组'''
		for group in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets]:
			group.update()
			group.draw(self.screen)

			


if __name__ == '__main__':
	 # 使用游戏类 创建一个游戏对象
	 game = PlaneGame()
	 # 开始游戏
	 game.start_game()

