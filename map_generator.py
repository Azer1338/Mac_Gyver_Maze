# -*- coding: utf-8 -*-

import pygame

#Constant
Sprite_size=43

width_screen=Sprite_size*15
height_screen=Sprite_size*15

fps= 30

color_water=(0,206,209)
#color_green=(100,155,0)
#color_white=(255,255,255)

class Monitor():
	
	def init_monitor(self):
		
		#initialisation of the pygame library
		pygame.init()
		
		#FPS - Frame Per Second Management
		self.fps_management()
		
		#Initialisation of the screen
		self.init_screen()
		
		#Initialisation of the map
		#Build walls
		wall1=Tile(1,1)
		wall1.blit(tile_surface,tile_surface_rect)
		
	def init_screen(self):
		#Creation of the first screen
		screen=pygame.display.set_mode((width_screen,height_screen))
		
		#Top title screen generation
		self.top_title_generation()
		
		#Fill background color
		screen.fill(color_water)
		
		#display the result
		pygame.display.flip()
		
		#Wait a bit to show correctly the main screen - ms
		pygame.time.delay(2000)
		
	def top_title_generation (self):
	
		#Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")
		
	def fps_management(self):
		#FPS Management
		global clock
		clock=pygame.time.Clock()

class Builder():
	def generator(self,object_to_create):
		#Generation of the path
		if object_to_create == wall:
			pass
			
			
class Tile():
	
	def __init__(self, pos_x,pos_y):
		#pos_x is the position left-right of the tile on the screen
		#pos_y is the position top-bottom of the tile on the screen
		pos_x_add_sprite = pos_x*Sprite_size + Sprite_size
		pos_y_add_sprite = pos_y*Sprite_size + Sprite_size
		
		#Creation of the graphical object tile
		tile_surface = pygame.Surface((Sprite_size,Sprite_size))
		#Creation of the graphical object tile as a rectangle
		tile_surface_rect=tile_surface.get_rect()
		
		#
		
		
def main():
	pass
	
if __name__ == '__main__':
	main()
