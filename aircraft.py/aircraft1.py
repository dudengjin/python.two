import pygame

pygame.init()  # 初始化方法

#  创建游戏屏幕
screen = pygame.display.set_mode((480,700))

# 加载游戏背景 	
bg = pygame.image.load("./images/background.png")

# 确定英雄位置
hero_rect = pygame.Rect(100,500,120,126)

# 绘制到屏幕上
screen.blit(bg,(0,0))

# 加载英雄
hero = pygame.image.load("./images/me1.png")
# 绘制到屏幕上
screen.blit(hero,hero_rect)
# 刷新屏幕
pygame.display.update()

clock = pygame.time.Clock()

# 确定英雄位置
# hero_rect = pygame.Rect(100,500,120,126)

i = 0 
y = 500 

hero_rect = pygame.Rect(100,y,120,126)

while True:
	i += 1 
	hero_rect.y -= 1
	# clock.tick(60)
	# hero_rect = pygame.Rect(100,y,120,126)
	if hero_rect.y + hero_rect.height <= 0:
		hero_rect.y = 700

	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	pygame.display.update()
	clock.tick(60)

	# 监听事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏....")
			pygame.quit()
			exit()

	'''
	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_RIGHT]:
		self.hero.speed = 2
	elif keys_pressed[pygame.K_RIGHT]:
		self.hero.speed = -2
	else:
		self.hero.speed = 0
	'''

pygame.quit() 


