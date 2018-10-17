# -*- coding: utf-8 -*-

import pygame

from sys import exit


#Constant
width_screen=600
height_screen=480

color_green=(100,155,0)
color_white=(255,255,255)

def main():
	#initialisation of the pygame library
	pygame.init()

	#Creation of the infinity loop
	running=True

	#Creation of the first screen
	screen=pygame.display.set_mode((width_screen,height_screen))

	#Definition of the main screen title
	pygame.display.set_caption("Mac Gyver Maze")

	#Launch the infinity loop
	while running == True:
		#Screen Exit - X on the top right of the screen
		for evt in pygame.event.get():
			if evt.type == pygame.QUIT:
				running=False
			endif

		#Fill background color
		screen.fill(color_green)

		#display the result
		pygame.display.flip()

	#Wait a bit to show correctly the main screen - ms
	#pygame.time.delay(2000)

	#endinf of the pygame library
	pygame.quit()
	#quit Python from sys library
	exit()

	return 0


if __name__ == '__main__':
	main()
