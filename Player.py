# -*- coding: utf-8 -*-

import pygame
import Maze
import numpy

import Tile


class Player():	
	#Class Attributes
	SPEED = 1
	
	def __init__(self, who,screen):
		
		#Initialisation
		self.perso = who
		self.screen_to_display = screen
		
		#Initialisation of the backpack
		self.backpack = []
		
		#Initial position of the icon
		if who == "Mac_Gyver":
			#Position
			self.pos_x_matrix =11
			self.pos_y_matrix =8
		else:
			#Position
			self.pos_x_matrix =13
			self.pos_y_matrix =13
		
		#Mesure of the matrix per side
		self.length_side_on_screen = screen.LENGTH_PER_SIDE - 1
		
		#Display the player on screen
		screen.screen_maze_matrix_updated[self.pos_x_matrix][self.pos_y_matrix] = self.perso
		
	def move_up(self,screen):
		#Character move up on the screen
		move = self.pos_y_matrix - Player.SPEED
		
		#Stay in the screen
		new_position= self.stay_in_frame(move,self.pos_y_matrix)
		
		#Event during walking on the way to go home
		if new_position != self.pos_y_matrix:
			self.action_on_motion("Y",new_position)

	def move_down(self,screen):
		#Character move down on the screen
		move = self.pos_y_matrix + Player.SPEED
		
		#Stay in the screen
		new_position= self.stay_in_frame(move,self.pos_y_matrix)
		
		#Event during walking on the way to go home
		if new_position != self.pos_y_matrix:
			self.action_on_motion("Y",new_position)
			
	def move_left(self,screen):
		#Character move left on the screen
		move = self.pos_x_matrix - Player.SPEED
		
		#Stay in the screen
		new_position= self.stay_in_frame(move,self.pos_x_matrix)
		
		#Event during walking on the way to go home
		if new_position != self.pos_x_matrix:
			self.action_on_motion("X",new_position)
		
	def move_right(self,screen):
		#Character move right on the screen	
		move = self.pos_x_matrix + Player.SPEED
		
		#Stay in the screen
		new_position = self.stay_in_frame(move,self.pos_x_matrix)
		
		#Event during walking on the way to go home
		if new_position != self.pos_x_matrix:
			self.action_on_motion("X",new_position)
			
		
	def stay_in_frame (self, new_pos, init_pos):
		#If move out of frame
		if new_pos >= self.screen_to_display.LENGTH_PER_SIDE or new_pos < 0 :
			new_pos = init_pos
		
		return new_pos
			
	def action_on_motion(self, axis, new_position):
		#On the next tile, the player can find:
		#If Wall, the player could go there. Stay on same tile		
		if axis == "X" :
			self.Check_next_tile(new_position, self.pos_y_matrix)
			
		elif axis == "Y" :
			self.Check_next_tile(self.pos_x_matrix, new_position)
			
		else:
			Print("Axis unknown")
		
	def Check_next_tile(self, Xpos_in_matrice, Ypos_in_matrice):
		
		if self.screen_to_display.screen_maze_matrix_updated[Xpos_in_matrice][Ypos_in_matrice] == "Wall" :
			print("/!\ Wall")
			print ("")
			Xpos_in_matrice = self.pos_x_matrix
			Ypos_in_matrice = self.pos_y_matrix
			
		else:
			if self.screen_to_display.screen_maze_matrix_updated[Xpos_in_matrice][Ypos_in_matrice] == "Path" :
				pass
				
			elif self.screen_to_display.screen_maze_matrix_updated[Xpos_in_matrice][Ypos_in_matrice] == "Guard" :
				
				print("Game-over")
				
			else: #An object
				#Add the object in the backpack
				self.backpack.append(self.screen_to_display.screen_maze_matrix_updated[Xpos_in_matrice][Ypos_in_matrice])
					
			#Replace the actual tile by a path
			self.screen_to_display.screen_maze_matrix_updated[self.pos_x_matrix][self.pos_y_matrix] = "Path"
			
			#Swap the new position with actual position
			self.pos_x_matrix = Xpos_in_matrice
			self.pos_y_matrix = Ypos_in_matrice
			
			#Place the player on the new position
			self.screen_to_display.screen_maze_matrix_updated[self.pos_x_matrix][self.pos_y_matrix] = self.perso
			
			print(self.backpack)
