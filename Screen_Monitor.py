# -*- coding: utf-8 -*-

import pygame
import os
import numpy

import Tile

class Screen_Monitor():
	
	#Class Attributes
	#Mesure of a Sprite
	SPRITE_SIZE=43
	#Mesure of a side of the screen
	LENGTH_PER_SIDE=15
	#Dimension of the screen
	WIDTH_SCREEN=SPRITE_SIZE*LENGTH_PER_SIDE
	HEIGHT_SCREEN=SPRITE_SIZE*LENGTH_PER_SIDE
	#Frame Per Screen
	FPS= 25
	#Color definition
	COLOR_WATER=(0,206,209)
	
	#Dictonnary Number on maze - Obj
	OBJ_ICON =	{ 	0	:	"Path",
					1 	:	"Wall",
					2	:	"Needle",
					3	:	"Syringe",
					5	:	"Tube",
					7	:	"Ether",
					8	:	"Mac_Gyver",
					88	:	"Guard"
				}
		
	def __init__(self):
		#Attribute
		self.screen = None
		self.victory_game = False
	
		#Initialisation of the pygame library
		pygame.init()
		
		#Creation of the gaming screen
		self.screen = pygame.display.set_mode((self.WIDTH_SCREEN,self.HEIGHT_SCREEN))
		
		#Top Title Generation
		self.top_title_generation()
		
		#FPS
		self.fps_management_init()

	def top_title_generation (self):
		#Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")

	def fps_management_init(self):
		#FPS Management
		self.clock = pygame.time.Clock()
		
	def fps_management(self):
		self.clock.tick(Screen_Monitor.FPS)

	def load_matrix(self, matrix):
		#Copy paste of the initial maze
		self.screen_maze_matrix = matrix.maze_matrix
		
		#Replace number par OBJ_ICON name
		for i in range(0,Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0,Screen_Monitor.LENGTH_PER_SIDE):
				self.screen_maze_matrix[i][j] = Screen_Monitor.OBJ_ICON[self.screen_maze_matrix[i][j]]
							
		#Copy paste
		self.screen_maze_matrix_updated= self.screen_maze_matrix
		
		#Affichage sur ecran
		pygame.display.flip()
		
	def initalise_screen(self):		
		#First : Background tiles
		for i in range(0,Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0,Screen_Monitor.LENGTH_PER_SIDE):
				self.draw(Tile.Tile(self.screen_maze_matrix[i][j],i,j))

		#Affichage sur ecran
		pygame.display.flip()
		
	def update_screen(self):		
		#First : Background tiles		
		for i in range(0,Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0,Screen_Monitor.LENGTH_PER_SIDE):
				self.draw(Tile.Tile(self.screen_maze_matrix_updated[i][j],i,j))
					
		#Affichage sur ecran
		pygame.display.flip()
		
		#Verify the victory
		if self.victory_game == True : 
			self.game_over_display()

	def draw(self,object_to_draw):
	
		#Load the pattern to draw
		pattern = object_to_draw.img_pattern
		pattern = pygame.transform.scale(pattern,(Screen_Monitor.SPRITE_SIZE,Screen_Monitor.SPRITE_SIZE))
		
		#x, y of the rectangle
		rect_x = object_to_draw.pos_x_matrix
		rect_y = object_to_draw.pos_y_matrix
		
		#Add a image of the object on the cell (var_x, var_y)
		self.screen.blit(pattern,(rect_x*Screen_Monitor.SPRITE_SIZE,rect_y*Screen_Monitor.SPRITE_SIZE))
			
	def display_backpack(self,player,screen):
		
		#Fill the screen with a single color
		self.screen.fill((100,110,150))
		
		#Write the player s backpack content
		font = pygame.font.Font(None, 24)
		backpack_player = font.render(str(numpy.array(player.backpack)),1,(255,255,255))
		self.screen.blit(backpack_player, (300, 300))
		
		#Let the screen visible during few seconds		
		pygame.time.delay(10000)
		pygame.display.flip()
		
	def game_over_display(self):
		#Fill the screen with a single color
		self.screen.fill((100,0,150))
		
		#Write the player s backpack content
		font = pygame.font.Font(None, 24)
		Game_over_title = font.render("GAME-OVER",1,(255,255,255))
		Victory_title = font.render("VICTORY",1,(255,255,255))
		self.screen.blit(Game_over_title, (300, 500))
		self.screen.blit(Victory_title, (300, 300))
		
		#Let the screen visible during few seconds		
		pygame.time.delay(10000)
		pygame.display.flip()
