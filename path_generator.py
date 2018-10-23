# -*- coding: utf-8 -*-

import pygame
import os
import numpy

import screen_generator

#CONSTANT
#Maze path definition
MAZE =	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,
		 1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


class Maze_builder():
	
	def __init__(self):
		#Attributes
		self.img_pattern, self.img_pattern_rect = screen_generator.Sprite_extract("floor-tiles-20x20.png",20,0,0)
		self.maze_matrix= None
		self.maze_list=MAZE
		
		#Create a 2d matrix
		self.maze_matrix = self.Creation_matrix_from_array(self.maze_list)
		
	def Creation_matrix_from_array(self,array):
		#Creation of a matrix
		self.maze_matrix=[array[i:i+screen_generator.LENGTH_PER_SIDE] for i in range(0,len(array),screen_generator.LENGTH_PER_SIDE)]

def main():
	pass
	
if __name__ == '__main__':
	main()
