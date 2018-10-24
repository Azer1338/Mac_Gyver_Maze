# -*- coding: utf-8 -*-

import pygame
import random
import Maze

import Tile


class Object():
				
	def __init__(self,what, screen):
		#Attributes
		self.pos_x_matrix = 0
		self.pos_y_matrix = 0
		
		#Mesure of the matrix per side
		self.length_side_on_screen = screen.LENGTH_PER_SIDE - 1
					
		#Initialise a random position
		self.random_position()
		
		#Make sure that the object are on the road
		self.object_on_path(screen.screen_maze_matrix)
		
		#Insertion of the objects in the screen matrix
		screen.screen_maze_matrix[self.pos_x_matrix][self.pos_y_matrix] = what
		
	def random_position(self):
		#Attribute a number between 0 and the max values on axes
		self.pos_x_matrix=random.randint(0,self.length_side_on_screen)
		self.pos_y_matrix=random.randint(0,self.length_side_on_screen)
		
	def object_on_path(self,matrix):
		#Make sure the object will be on the path (available space)
		while not matrix[self.pos_y_matrix][self.pos_x_matrix] == "Path":
			self.random_position()
