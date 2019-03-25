import pygame

pygame.init()

screen = pygame.display.set_mode([1000,1000])
clock = pygame.time.Clock()


while True:
	pygame.display.flip()
	clock.tick(20)
	
pygame.quit()
