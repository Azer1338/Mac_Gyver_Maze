# -*- coding: utf-8 -*-

import pygame
import random
import map_generator


class Object():
	
	def __init__(self, what):
		# Link the kind of object with the picture
		if what=="Needle":
			#Icon
			self.object_icon,self.object_icon_rect = map_generator.load_png("aiguille.png",False)
		elif what=="Syringe":
			#Icon
			self.object_icon,self.object_icon_rect = map_generator.load_png("seringue.png",False)
		elif what=="Tube":
			#Icon
			self.object_icon,self.object_icon_rect = map_generator.load_png("tube_plastique.png",False)
		elif what=="Ether":
			#Icon
			self.object_icon,self.object_icon_rect = map_generator.load_png("ether.png",False)
		else:
			Print("Impossible to create")
			
		#Initialise a random position
		self.random_position()

	def object_on_path(self,matrix):
		#Check if the object is yes or not on the path
		while matrix[self.pos_y_obj_matrix][self.pos_x_obj_matrix] == 1:
			self.random_position()
			
	def random_position(self):
		#Attribute a number between 0 and the max values on axes
		self.pos_x_obj_matrix=random.randint(0,map_generator.side_square_screen_mesure-1)
		self.pos_y_obj_matrix=random.randint(0,map_generator.side_square_screen_mesure-1)
		
		self.pos_x_obj=self.pos_x_obj_matrix*map_generator.Sprite_size
		self.pos_y_obj=self.pos_y_obj_matrix*map_generator.Sprite_size

	
def main():
	pass
	
if __name__ == '__main__':
	main()
