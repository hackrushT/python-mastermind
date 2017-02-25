import pygame
from pygame.locals import *
import time
import random

pygame.init ()

#Colours
white = (255,255,255,128)
black = (0,0,0,128)
brown = (176,79,46,128)


#Global Variables
TRANSPARENT = (255,0,255)

disp_width = 550
disp_height = 700


#GameDisplay
gameDisplay = pygame.display.set_mode ((disp_width, disp_height))
pygame.display.set_caption ('Mastermind')

background = pygame.image.load ("images/bg.jpg")
clock = pygame.time.Clock ()


def drawPeg (x,y):

	surf = pygame.Surface ((200,200))
	surf.fill (TRANSPARENT)
	surf.set_colorkey (TRANSPARENT)
	pygame.draw.circle (surf, black, (102,102), 20)
	pygame.draw.circle (surf, white, (99,99), 20)
	pygame.draw.circle (surf, (176,79,46), (100,100), 20)
	pygame.draw.circle (gameDisplay, (0,0,0), (x,y), 15)
	pygame.draw.circle (gameDisplay, (176,79,46), (x,y), 13)

	surf.set_alpha (128)
	
	gameDisplay.blit (surf, (x-100,y-100,100,100))
	pygame.draw.circle (gameDisplay, (0,0,0), (x,y), 6)

#Main Gameloop
def mainloop ():

	exit = False

	while not exit:

		for event in pygame.event.get ():
			if event.type == pygame.QUIT:
				exit = True

		gameDisplay.blit (background, (0,0))
		y = 600
		for i in range (10):
			x = 125
			for j in range (4):
				drawPeg (x,y)
				x += 50
			y -= 50

		pygame.display.update ()

	pygame.quit ()
	quit ()

#main
mainloop ()
