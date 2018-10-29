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
		
		#Top title generation
		self.top_title_generation()
		
		#FPS initialisation
		self.fps_management_init()

	def top_title_generation (self):
		#Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")

	def fps_management_init(self):
		#FPS Management
		self.clock = pygame.time.Clock()
		
	def fps_management(self):
		#Check the FPS at every screen update
		self.clock.tick(Screen_Monitor.FPS)

	def load_matrix(self, matrix):
		#Initialise a proper maze_matrix for futures modifications
		self.screen_maze_matrix = [[0]*Screen_Monitor.LENGTH_PER_SIDE for i in range(Screen_Monitor.LENGTH_PER_SIDE)]
		#Copy paste initial maze_matrix to maze_matrix in order
		self.screen_maze_matrix_updated = [[0]*Screen_Monitor.LENGTH_PER_SIDE for i in range(Screen_Monitor.LENGTH_PER_SIDE)]
		
		#Replace number par OBJ_ICON name - minus 1 to respect the dimension of the table
		for i in range(0,Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0,Screen_Monitor.LENGTH_PER_SIDE):
				self.screen_maze_matrix[i][j] = Screen_Monitor.OBJ_ICON[matrix.maze_matrix[i][j]]
				self.screen_maze_matrix_updated[i][j] = Screen_Monitor.OBJ_ICON[matrix.maze_matrix[i][j]]

		#Affichage sur ecran
		pygame.display.flip()
		
	def initialise_screen(self):		
		#First : Background tiles
		for i in range(0,Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0,Screen_Monitor.LENGTH_PER_SIDE):
				self.draw(Tile.Tile(self.screen_maze_matrix[i][j],i,j))

		#Affichage sur ecran
		pygame.display.flip()
		
	def update_screen(self):
		#FPS management
		self.fps_management_init()	
		
		#First : Background tiles		
		for i in range(0,Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0,Screen_Monitor.LENGTH_PER_SIDE):
				if self.screen_maze_matrix_updated[i][j] != self.screen_maze_matrix[i][j]:
					print("{} - Fuck you - {}".format(self.screen_maze_matrix_updated[i][j],self.screen_maze_matrix[i][j]))
					self.draw(Tile.Tile(self.screen_maze_matrix_updated[i][j],i,j))
					#Make sure that the loop will be use for modification only
				self.screen_maze_matrix_updated[i][j] = self.screen_maze_matrix[i][j]
					
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
		pygame.display.flip()
		pygame.time.delay(10)
