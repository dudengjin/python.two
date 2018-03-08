import pygame

pygame.init()  # 初始化方法

#  创建游戏屏幕
screen = pygame.display.set_mode((480,700))

hero_rect = pygame.Rect(100,500,120,126)

# 加载图片 	
bg = pygame.image.load("./images/background.png")
# 绘制到屏幕
screen.blit(bg,(0,0))

# 加载英雄
bg = pygame.image.load("./images/me1.png")
# 绘制到屏幕上
screen.blit(hero,(200,500))
# 刷新屏幕
pygame.display.update()


while True:
	clock.tick(60)


if hero_rect.y <= 0:
	hero_rect.y = 700

pygame.display.update()	
	

pygame.quit() 



