import pygame
import random
pygame.init()

screen = pygame.display.set_mode([600,600])
clock = pygame.time.Clock()
black = [0,0,0]
white = [255,255,255]

def getQuad(pos_x, pos_y):
	if pos_x >= 300:
		if pos_y <= 300:
			return 1
		else:
			return 4
	else:
		if pos_y <= 300:
			return 2
		else:
			return 3

pos_x = 300
pos_y = 300
nw = 0
ne = 0
sw = 0
se = 0

try:
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:  
				pygame.quit()

				
		screen.fill(white)
		pygame.draw.line(screen, black, [0,300], [600,300])
		pygame.draw.line(screen, black, [300,0], [300,600])
		pygame.draw.rect(screen, black, [pos_x, pos_y, 10, 10])	#SURFACE, COLOR, [TOP LEFT X, TOP LEFT Y, X WIDTH, Y HEIGHT]
		quad = getQuad(pos_x + 5, pos_y + 5)
		if quad == 1:
			ne += 1
		elif quad == 2:
			nw += 1
		elif quad == 3:
			sw += 1
		else:
			se += 1
		totalSteps = ne+nw+sw+se
		ne_angle = 2*3.14*ne/totalSteps
		nw_angle = 2*3.14*nw/totalSteps
		sw_angle = 2*3.14*sw/totalSteps
		se_angle = 2*3.14*se/totalSteps
		print(ne_angle)
		pygame.draw.arc(screen, black, [150,150,50,50], 0, ne_angle)
		pygame.draw.arc(screen, [50,50,50], [150,150,50,50], ne_angle, ne_angle+ nw_angle)
		pygame.draw.arc(screen, [100,100,100], [150,150,50,50], ne_angle+ nw_angle, ne_angle+ nw_angle+sw_angle)
		pygame.draw.arc(screen, [150,150,150], [150,150,50,50], ne_angle+ nw_angle+sw_angle, 2*3.14)




		pygame.display.flip()
		clock.tick(60)
		pos_x += random.randint(-5,5)
		pos_y += random.randint(-5,5)

except:
	pass

