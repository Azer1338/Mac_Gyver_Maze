# -*- coding: utf-8 -*-

import pygame
import os

#CONSTANT
#Mesure of a Sprite
SPRITE_SIZE=43
#Mesure of a side of the screen
LENGTH_PER_SIDE=15
#Dimension of the screen
WIDTH_SCREEN=SPRITE_SIZE*LENGTH_PER_SIDE
HEIGHT_SCREEN=SPRITE_SIZE*LENGTH_PER_SIDE
#Frame Per Screen
FPS= 30
#Color definition
COLOR_WATER=(0,206,209)

class Screen_Monitor():

	
	def __init__(self):
		#Attribute
		self.screen = None
		self.var_x = 0
		self.var_y = 0
	
		#Initialisation of the pygame library
		pygame.init()
		
		#FPS - Frame Per Second Management
		self.fps_management()
		
		#Creation of the first screen
		self.screen = pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))
		
		#Top Title Generation
		self.top_title_generation()
		
		#Initialize and update the background
		self.screen.fill(COLOR_WATER)
		self.display_on_screen()
		
	def update_background_screen(self,maze):
		#Fill background color
		self.screen.fill(COLOR_WATER)
		
		#Maze generation
		maze.draw(self.screen,main.side_square_screen_mesure,main.Sprite_size)

	def top_title_generation (self):
		#Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")
		
	def display_on_screen(self):
		#display the result
		pygame.display.flip()
		
		#Wait a bit to show correctly the main screen - ms
		pygame.time.delay(300)

	def fps_management(self):
		#FPS Management
		global clock
		clock=pygame.time.Clock()
		
	def draw_path(self,object_to_draw):
		#Initialisation
		self.var_x=self.var_y=0
		
		#Load the path pattern from an extract sprite sheet
		self.path_pattern = object_to_draw.img_pattern
		self.path_pattern_rect = object_to_draw.img_pattern_rect
		
		#Draw the maze
		if object_to_draw == Maze_path:
			#Go through the MAZE path definition in order to display the path on the screen
			for i in range(0,LENGTH_PER_SIDE*LENGTH_PER_SIDE):
				#Determine 0 as a path pattern - 1 as nothing
				if object_to_draw.maze_list[self.var_x +self.var_y*LENGTH_PER_SIDE]==0:
					#Add a image of the object on the cell (var_x, var_y)
					self.screen.blit(self.path_pattern,(self.var_x*SPRITE_SIZE,self.var_y*SPRITE_SIZE))
							
				#When var_x reach the edge of the screen, var_y is inscreased by 1 and var_x is reinitialised
				if self.var_x > (LENGTH_PER_SIDE-1):
					self.var_x = 0
					self.var_y +=1
				else:
					self.var_x+=1		
		#Draw other object
		else:
			#x, y of the rect
			self.var_x = object_to_draw.pos_x_obj_matrix
			self.var_y = object_to_draw.pos_x_obj_matrix
			
			#Add a image of the object on the cell (var_x, var_y)
			self.screen.blit(self.path_pattern,(self.var_x*SPRITE_SIZE,self.var_y*SPRITE_SIZE))
		


def Sprite_extract(Sprite_sheet_filename,len_sprt_size,pos_cell_x,pos_cell_y):
	#len_sprt_size = Sprite size in Sprite_sheet_filname file

	#Sprite position in Sprite_sheet_filname file
	Pos_x = pos_cell_x*len_sprt_size
	Pos_y = pos_cell_y*len_sprt_size
	
	#Load the sprite sheet
	sprite_sheet,sprite_sheet_rect = load_png(Sprite_sheet_filename,True)

	#Locate the sprite in the sprite sheet - Rect(left, top, width, height) -> Rect
	sprite_sheet.set_clip(pygame.Rect(Pos_x, Pos_y, len_sprt_size, len_sprt_size))
	
	#Extract the sprite
	sprit_icon = sprite_sheet.subsurface(sprite_sheet.get_clip())
	sprit_icon= pygame.transform.smoothscale(sprit_icon,(SPRITE_SIZE,SPRITE_SIZE))
	
	return sprit_icon,sprit_icon.get_rect()
		
		
	
def load_png(name,from_sprite_sheet):
	#Load a picture from the repertory RESSOURCE and return a picture object
	fullname=os.path.join('./ressource/', name)
	image = pygame.image.load(fullname)
	
	if image.get_alpha is None:
		image = image.convert()
	else:
		image = image.convert_alpha()
		
	#Adjust the image if it is not coming from a sprite sheet
	if from_sprite_sheet == False:
		image = pygame.transform.smoothscale(image,(SPRITE_SIZE,SPRITE_SIZE))
	
	return image, image.get_rect()
		
		
def main():
	pass
	
if __name__ == '__main__':
	main()
