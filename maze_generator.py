# -*- coding: utf-8 -*-

import pygame
import os

import map_generator

#CONSTANT
#Maze path definition
MAZE =	[1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,
		 1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
		 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,
		 1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
		 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


class Maze():
	
	def __init__(self):
		#Attributes
		self.var_x=0
		self.var_y=0
		
	def draw(self, display_path, square_side_mesure,Sprit_size):
		#Load the path pattern from an extract sprite sheet
		path_pattern,path_pattern_rect = map_generator.Sprite_extract("floor-tiles-20x20.png")
		
		#Go through the MAZE path definition in order to display the path on the screen
		for i in range(0,square_side_mesure*square_side_mesure):
			#Determine 0 as a path pattern - 1 as nothing
			if MAZE[self.var_x +self.var_y*square_side_mesure]==0:
				#Add a path pattern on the cell (var_x, var_y)
				display_path.blit(path_pattern,(self.var_x*Sprit_size,self.var_y*Sprit_size))
						
			#When var_x reach the edge of the screen, var_y is inscreased by 1 and var_x is reinitialised
			if self.var_x > (square_side_mesure-1):
				self.var_x = 0
				self.var_y +=1
			else:
				self.var_x+=1
		
		
def main():
	pass
	
if __name__ == '__main__':
	main()
