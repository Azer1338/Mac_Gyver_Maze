# -*- coding: utf-8 -*-

import pygame
import os

import maze_generator
import actors_generator

#CONSTANT
#Mesure of a Sprite
Sprite_size=43
#Mesure of a side of the screen
side_square_screen_mesure=15
#Dimension of the screen
width_screen=Sprite_size*side_square_screen_mesure
height_screen=Sprite_size*side_square_screen_mesure
#Frame Per Screen
fps= 30
#Color definition
color_water=(0,206,209)

class Monitor():
	#Attribute
	screen = None
	
	def __init__(self):
		#Initialisation of the pygame library
		pygame.init()
		
		#FPS - Frame Per Second Management
		self.fps_management()
		
		#Creation of the first screen
		self.screen=pygame.display.set_mode((width_screen,height_screen))
		
		#Top Title Generation
		self.top_title_generation()
		
		#Initialize and update the background + maze
		self.update_background_screen()
		
	def update_background_screen(self):
		#Fill background color
		self.screen.fill(color_water)
		
		#Maze generation
		maze_on_screen = maze_generator.Maze()
		maze_on_screen.draw(self.screen,side_square_screen_mesure,Sprite_size)

	def top_title_generation (self):
		#Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")
		
	def display_on_screen(self):
		#display the result
		pygame.display.flip()
		
		#Wait a bit to show correctly the main screen - ms
		pygame.time.delay(000)

	def fps_management(self):
		#FPS Management
		global clock
		clock=pygame.time.Clock()
		
	
def Sprite_extract(Sprite_sheet_filename):
	#Sprite size in Sprite_sheet_filname file
	len_sprt_size = 20
	
	#Sprite position in Sprite_sheet_filname file
	Pos_x = 0*len_sprt_size
	Pos_y = 0*len_sprt_size
	
	#Load the sprite sheet
	sprite_sheet,sprite_sheet_rect = load_png(Sprite_sheet_filename)

	#Locate the sprite in the sprite sheet - Rect(left, top, width, height) -> Rect
	sprite_sheet.set_clip(pygame.Rect(Pos_x, Pos_y, len_sprt_size, len_sprt_size))
	
	#Extract the sprite
	sprit_icon = sprite_sheet.subsurface(sprite_sheet.get_clip())
	sprit_icon= pygame.transform.smoothscale(sprit_icon,(Sprite_size,Sprite_size))
	
	return sprit_icon,sprit_icon.get_rect()
		
		
	
def load_png(name):
	#Load a picture from the repertory RESSOURCE and return a picture object
	fullname=os.path.join('./ressource/', name)
	image = pygame.image.load(fullname)
	
	if image.get_alpha is None:
		image = image.convert()
	else:
		image = image.convert_alpha()
	
	return image, image.get_rect()
		
		
def main():
	pass
	
if __name__ == '__main__':
	main()
