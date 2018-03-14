import pygame
import random

# 游戏屏幕大小 
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 敌机的定时器事件常量(产生敌机)
CREATE_ENEMT_EVENT = pygame.USEREVENT
# 定义一个事件常量(发射子弹)
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
	'''游戏精灵基类'''
	def __init__(self,image_name,speed=1):
		# 调用父类的初始化方法
		super().__init__()
		
		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸:image的get_rect()方法,可以返回pygame.rect(0,0,宽,高)的对象
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed
 
	def update(self):
		# 默认垂直方向移动
		self.rect.y += self.speed

class BackGround(GameSprite):
	'''游戏背景精灵类'''
	def __init__(self,is_alt = False):
		
		image_name = "images/background.png"
		super().__init__(image_name)
		# 判断是否交替图片,如果是,将图片设置到屏幕顶部
		if is_alt:
			self.rect.y = -self.rect.height


	def update(self):
		# 调用父类的方法实现
		super().update()
		# 判断是否移出屏幕,如果移出屏幕,将图像设置到屏幕上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height

class Enemy(GameSprite):
	'''敌机精灵'''	
	def __init__(self):
		# 调用父类方法,创建敌机精灵,并且指定敌机图像
		super().__init__("./images/enemy1.png")
		
		# 设置敌机初始速度,随机初始速度1~3
		self.speed = random.randint(1, 3)
		# 设置敌机的随机初始位置
		self.rect.bottom = 0
		man_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, man_x)

	def update(self):
		# 调用父类方法,让敌机在垂直方向运动
		super().update()
		# 判断是否飞出屏幕,如果是,需要将敌机从精灵组删除
		if self.rect.y >= SCREEN_RECT.height:
			print("敌机飞出屏幕...")
			# 将精灵从精灵组删除
			self.kill()
			
class Hero(GameSprite):
	'''英雄精灵类'''
	def __init__(self):
		# 英雄的初始位置设置为0
		super().__init__("./images/me1.png",0)
		# 设置初始位置,这是让我英雄x轴的中心点等于屏幕x轴
		self.rect.centerx = SCREEN_RECT.centerx
		# 这是设置我飞机的y轴
		self.rect.bottom = SCREEN_RECT.bottom - 120
		
		self.bullets = pygame.sprite.Group()
		
	def update(self):
		# 飞机水平移动
		self.rect.x += self.speed
		# 判断屏幕边界
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right	
		
	
	def fire(self):
		# 英雄的方法,发射子弹,是一个动作,是一个行为
		print("发射子弹...")

		for i in (1,2,3):
			# 创建子弹精灵
			bullet = Bullet()
			# 设置精灵位置
			bullet.rect.bottom = self.rect.y - 20*i
			bullet.rect.centerx = self.rect.centerx
			# 将精灵添加到精灵组
			self.bullets.add(bullet)
	

class Bullet(GameSprite):
	'''子弹精灵'''
	def __init__(self):
		super().__init__("./images/bullet1.png",-2)

	def update(self):
		super().update()
		# 判断是否超出屏幕
		if self.rect.bottom < 0:
			self.kill()


