# -*- coding: utf-8 -*-

import pygame
import Maze

import Tile


class Player():
	
	#Class Attributes
	SPEED = 1
	
	def __init__(self, who,screen):
		
		#Initialisation
		self.perso = who
		self.screen_to_display = screen
		
		#Initial position of the icon
		if who == "Mac_Gyver":
			#Position
			self.pos_x_matrix =1
			self.pos_y_matrix =2
		else:
			#Position
			self.pos_x_matrix =13
			self.pos_y_matrix =13
			
		#Future position of the player on the matrix
		self.new_pos_x_matrix = self.pos_x_matrix
		self.new_pos_y_matrix = self.pos_y_matrix
		
		#Mesure of the matrix per side
		self.length_side_on_screen = screen.LENGTH_PER_SIDE - 1
		
		self.modification_of_the_screen_matrix(self.perso , self.screen_to_display )
		
	def modification_of_the_screen_matrix(self,what,screen):
		#Insertion of the player in the screen matrix
		screen.screen_maze_matrix[self.pos_y_matrix][self.pos_x_matrix] = "Path"
		screen.screen_maze_matrix[self.new_pos_y_matrix][self.new_pos_x_matrix] = self.perso

	def move_up(self):
		#Character move up on the screen
		self.new_pos_y_matrix= self.pos_y_matrix - Player.SPEED
		self.pos_y_matrix = self.stay_on_screen(self.pos_y_matrix,self.new_pos_y_matrix)
	
	def move_down(self):
		#Character move down on the screen
		self.new_pos_y_matrix= self.pos_y_matrix + Player.SPEED
		self.pos_y_matrix = self.stay_on_screen(self.pos_y_matrix,self.new_pos_y_matrix)
		
	def move_left(self):
		#Character move left on the screen
		self.new_pos_x_matrix= self.pos_x_matrix - Player.SPEED
		self.pos_x_matrix = self.stay_on_screen(self.pos_x_matrix,self.new_pos_x_matrix)
		
	def move_right(self):
		#Character move right on the screen	
		self.new_pos_x_matrix= self.pos_x_matrix + Player.SPEED
		self.pos_x_matrix = self.stay_on_screen(self.pos_x_matrix,self.new_pos_x_matrix)

	def stay_on_screen(self, init_position, new_position):
		#Limit Character moves on positive axis
		if new_position > self.length_side_on_screen:
			position_into_screen = init_position
		#Limit Character moves on negative axis
		elif new_position < 0:
			position_into_screen = init_position
		else :
			position_into_screen = new_position
			#Update the screen matrix
			self.modification_of_the_screen_matrix(self.perso , self.screen_to_display )
		
		return position_into_screen
		
	def catch_an_object (self):
		
