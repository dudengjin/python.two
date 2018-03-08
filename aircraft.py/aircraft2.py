import pygame

clock = pygame.time.Clock()
i = 0 

while True:
	clock.tick(1)
	print(i)
	i += 1







clock.tick(60)

hero_rect.y -= 1

if hero_rect.y <= 0:
	hero_rect.y = 700

screen.blit(bg(0,0))	
screen.blit(hero,hero_rect)
pygame.display.update()	