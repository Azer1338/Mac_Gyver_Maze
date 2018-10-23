# -*- coding: utf-8 -*-

import pygame
import random
import screen_generator


class Object_builder():
	
	def __init__(self, what):
		#load the picture/rectangle of the object
		self.img_pattern = None
		self.img_pattern_rect = None
		
		#Position in the matrix
		self.pos_x_obj_matrix = None
		self.pos_y_obj_matrix = None
		
		# Link the kind of object with the picture
		if what=="Needle":
			#Icon
			self.img_pattern,self.img_pattern_rect = screen_generator.load_png("aiguille.png",False)
		elif what=="Syringe":
			#Icon
			self.img_pattern,self.img_pattern_rect = screen_generator.load_png("seringue.png",False)
		elif what=="Tube":
			#Icon
			self.img_pattern,self.img_pattern_rect = screen_generator.load_png("tube_plastique.png",False)
		elif what=="Ether":
			#Icon
			self.img_pattern,self.img_pattern_rect = screen_generator.load_png("ether.png",False)
		else:
			Print("Object unknown - Impossible to create")
			
		#Initialise a random position
		self.random_position()
		
	def random_position(self):
		#Attribute a number between 0 and the max values on axes
		self.pos_x_obj_matrix=random.randint(0,screen_generator.LENGTH_PER_SIDE-1)
		self.pos_y_obj_matrix=random.randint(0,screen_generator.LENGTH_PER_SIDE-1)
		
		self.pos_x_obj_matrix=self.pos_x_obj_matrix*screen_generator.SPRITE_SIZE
		self.pos_y_obj_matrix=self.pos_y_obj_matrix*screen_generator.SPRITE_SIZE
		
	def object_on_path(self,matrix):
		#Check if the object is yes or not on the path
		while matrix[self.pos_y_obj_matrix][self.pos_x_obj_matrix] == 1:
			self.random_position()

	
def main():
	pass
	
if __name__ == '__main__':
	main()
