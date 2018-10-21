# -*- coding: utf-8 -*-

import pygame
import os

#Constant
#Mesure of an Sprite
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
#color_green=(100,155,0)
#color_white=(255,255,255)

MAZE =	[1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,
		1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

class Monitor():
	
	def __init__(self):
		
		#initialisation of the pygame library
		pygame.init()
		
		#FPS - Frame Per Second Management
		self.fps_management()
		
		#Creation of the first screen
		self.screen=pygame.display.set_mode((width_screen,height_screen))
		
		#Fill background color
		self.screen.fill(color_water)
		
		#Top Title Generation
		self.top_title_generation()
		
		#Show the results
		self.display_on_screen()

	def top_title_generation (self):
	
		#Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")
		
	def display_on_screen(self):
		#display the result
		pygame.display.flip()
		
		#Wait a bit to show correctly the main screen - ms
		pygame.time.delay(1000)

	def fps_management(self):
		#FPS Management
		global clock
		clock=pygame.time.Clock()
		
	def map_generator(self):
		#Attributes
		var_x=0
		var_y=0
		
		#Load the path pattern
		path_pattern,path_pattern_rect=load_png('MacGyver.png')
		#look into the maze
		for i in range(0,side_square_screen_mesure*side_square_screen_mesure):
			#Determine if 1 = Wall or 0 for nothing in the maze definition
			if MAZE[var_x +var_y*side_square_screen_mesure]==1:
				self.screen.blit(path_pattern,(var_x*Sprite_size,var_y*Sprite_size))
			
			var_x+=1
			if var_x > (side_square_screen_mesure-1):
				var_x = 0
				var_y +=1
				
			print("var_x = {},var_y = {}".format(var_x,var_y))
				
		#determine if 1 = Wall or 0 for nothing in the maze definition
				
		#Show the results
		self.display_on_screen()
		
def other():
		#Path
		#Creation of the graphical object tile
		tile_surface1 = pygame.Surface((Sprite_size,Sprite_size))
		#Color of the graphical object tile
		tile_surface1.fill((0,50,0))
		#Creation of the graphical object tile as a rectangle
		tile_surface_rect1 = tile_surface1.get_rect()
		#Position of the tile
		tile_surface_rect1.x=Sprite_size*0
		tile_surface_rect1.y=Sprite_size*1	
		#Creation of the graphical object tile
		tile_surface2 = pygame.Surface((Sprite_size,Sprite_size))
		
		#Color of the graphical object tile
		tile_surface2.fill((0,50,0))
		#Creation of the graphical object tile as a rectangle
		tile_surface_rect2 = tile_surface2.get_rect()
		#Position of the tile
		tile_surface_rect2.x=Sprite_size*1
		tile_surface_rect2.y=Sprite_size*1
		#Creation of the graphical object tile
		tile_surface3 = pygame.Surface((Sprite_size,Sprite_size))
		#Color of the graphical object tile
		tile_surface3.fill((0,50,0))
		#Creation of the graphical object tile as a rectangle
		tile_surface_rect3 = tile_surface3.get_rect()
		#Position of the tile
		tile_surface_rect3.x=Sprite_size*2
		tile_surface_rect3.y=Sprite_size*1
		#Creation of the graphical object tile
		tile_surface4 = pygame.Surface((Sprite_size,Sprite_size))
		#Color of the graphical object tile
		tile_surface4.fill((0,50,0))
		#Creation of the graphical object tile as a rectangle
		tile_surface_rect4 = tile_surface4.get_rect()
		#Position of the tile
		tile_surface_rect4.x=Sprite_size*3
		tile_surface_rect4.y=Sprite_size*1
		#Creation of the graphical object tile
		tile_surface5 = pygame.Surface((Sprite_size,Sprite_size))
		#Color of the graphical object tile
		tile_surface5.fill((0,50,0))
		#Creation of the graphical object tile as a rectangle
		tile_surface_rect5 = tile_surface5.get_rect()
		#Position of the tile
		tile_surface_rect5.x=Sprite_size*4
		tile_surface_rect5.y=Sprite_size*1
		#Blit of the path
		screen.blit(tile_surface1,tile_surface_rect1)
		screen.blit(tile_surface2,tile_surface_rect2)
		screen.blit(tile_surface3,tile_surface_rect3)
		screen.blit(tile_surface4,tile_surface_rect4)
		screen.blit(tile_surface5,tile_surface_rect5)
		
		#Mac Gyver
		#Load the icon
		mac_gyver_icon=pygame.image.load('./ressource/MacGyver.png')
		mac_gyver_icon=mac_gyver_icon.convert()
		mac_gyver_icon= pygame.transform.smoothscale(mac_gyver_icon,(Sprite_size,Sprite_size))
		#Creation of the icon as a rectangle
		mac_gyver_icon_rect=mac_gyver_icon.get_rect()
		#Position of the icon
		mac_gyver_icon_rect.x=Sprite_size*0
		mac_gyver_icon_rect.y=Sprite_size*1
		#Blit of the icon
		screen.blit(mac_gyver_icon,mac_gyver_icon_rect)
		
		#Gard
		#Load the icon
		gard_icon=pygame.image.load("./ressource/Gardien.png")
		gard_icon=gard_icon.convert()
		gard_icon= pygame.transform.smoothscale(gard_icon,(Sprite_size,Sprite_size))
		#Creation of the icon as a rectangle
		gard_icon_rect=gard_icon.get_rect()
		#Position of the icon
		gard_icon_rect.x=Sprite_size*4
		gard_icon_rect.y=Sprite_size*1
		#Blit of the icon
		screen.blit(gard_icon,gard_icon_rect)
		
		#Syringe
		#Load the icon
		syringe_icon=pygame.image.load("./ressource/seringue.png")
		syringe_icon=syringe_icon.convert()
		syringe_icon= pygame.transform.smoothscale(syringe_icon,(int(Sprite_size/2),int(Sprite_size/2)))
		#Creation of the icon as a rectangle
		syringe_icon_rect=syringe_icon.get_rect()
		#Position of the icon
		syringe_icon_rect.x=Sprite_size*2
		syringe_icon_rect.y=Sprite_size*1
		#Blit of the icon
		screen.blit(syringe_icon,syringe_icon_rect)
	
	
def load_png(name):
	#Load a picture from the repertory RESSOURCES and return a picture object
	fullname=os.path.join('./ressource/', name)
	print(fullname)
	image = pygame.image.load(fullname)
	
	if image.get_alpha is None:
		image = image.convert()
	else:
		image = image.convert_alpha()
		
	return image, image.get_rect()
	

def Sprite_extract(Sprite_sheet_filename,Pos_x,Pos_y):
	#Load the sprite sheet
	sprite_sheet = pygame.image.load(Sprite_sheet_filename)

	sprite_sheet.set_clip(pygame.Rect(Pos_x, Pos_y, LEN_SPRT_X, LEN_SPRT_Y)) #Locate the sprite you want
	draw_me = sheet.subsurface(sheet.get_clip()) #Extract the sprite you want

	backdrop = pygame.Rect(0, 0, SCREEN_X, SCREEN_Y) #Create the whole screen so you can draw on it

	screen.blit(draw_me,backdrop) #'Blit' on the backdrop
	pygame.display.flip()
	#Draw the sprite on the screen
		
		
def main():
	pass
	
if __name__ == '__main__':
	main()
