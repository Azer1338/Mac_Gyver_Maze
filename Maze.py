# -*- coding: utf-8 -*-

import pygame
import os
import numpy

import Tile

#CONSTANT
#Maze path definition
#8  = Player Departure
#88 = Guard - Arrival
MAZE =	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		 1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 ]
		 

class Maze():
	
	def __init__(self, screen):
		
		#Attributes
		#Mesure of the matrix per side
		self.length_side_on_screen = screen.LENGTH_PER_SIDE
		
		#Create a 2d matrix
		self.maze_matrix = self.Creation_matrix_from_array(MAZE)
		
	def Creation_matrix_from_array(self,array):
		#Creation of a matrix
		matrix = [array[i:i+self.length_side_on_screen] for i in range(0,len(array),self.length_side_on_screen)]
		
		return matrix

