# -*- coding: utf-8 -*-

import pygame

from sys import exit


#Constant
width_screen=600
height_screen=480
fps= 30

color_green=(100,155,0)
color_white=(255,255,255)

def action_event(event):
	#Keyboard pressed
	if event.type==pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:
			print("Down")
	
	#Keyboard released
	if event.type==pygame.KEYUP:
		if event.key == pygame.K_SPACE:
			print("Up")

def main():
	#initialisation of the pygame library
	pygame.init()

	#Creation of the infinity loop
	running=True

	#Creation of the first screen
	screen=pygame.display.set_mode((width_screen,height_screen))

	#Definition of the main screen title
	pygame.display.set_caption("Mac Gyver Maze")
	
	#FPS Management
	clock=pygame.time.Clock()
	
	#Creation of a rectangle
	#Creation of the dimension
	box_surface=pygame.Surface((20,20))
	#Surface color
	box_surface.fill((0,20,100))
	#Kind of the surface = rectangle
	box_rect=box_surface.get_rect()
	#Position
	box_rect.center=((300,200))
	
	print("x={0}, y={1}, w={2},h={3}".format(box_rect.x,box_rect.y,box_rect.w,box_rect.w))

	#Launch the infinity loop
	while running == True:
		
		#FPS management
		delta_ms=clock.tick(fps)
		delta_s=delta_ms/1000
		
		print("Delta_ms= {}".format(delta_s))
		
		#Event management
		for evt in pygame.event.get():
			#Screen Exit - X on the top right of the screen
			if evt.type == pygame.QUIT:
				running=False
			
			#Keyboard pressed
			if evt.type==pygame.KEYDOWN:
				if evt.key == pygame.K_ESCAPE:
					running=False
					
			#Keyboard management
			action_event(evt)		

		#Fill background color
		screen.fill(color_green)
		
		#Surface management
		screen.blit(box_surface,box_rect)

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
