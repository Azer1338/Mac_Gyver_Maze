# -*- coding: utf-8 -*-

import pygame
import os

class Tile():
	#Class Attributes
	PIC_ICON =	{	"Wall"		: "floor-tiles-20x20.png",
					"Path"		: "floor-tiles-20x20.png",
					"Needle" 	: "aiguille.png",
					"Syringe"	: "seringue.png",
					"Tube" 		: "tube_plastique.png",
					"Ether" 	: "ether.png",
					"Mac_Gyver" : "MacGyver.png",
					"Guard"		: "Gardien.png"
				}
				
	def __init__(self, obj_what):
		
		#load the picture/rectangle of the object
		self.img_pattern = None
		self.img_pattern_rect = None

		# Link the kind of object with the icon picture
		if obj_what == "Wall":
			#Path case - Sprite sheet need to be loaded differently
			self.Sprite_extract(Tile.PIC_ICON[obj_what],20,0,0)
		elif obj_what == "Path":
			#Path case - Sprite sheet need to be loaded differently
			self.Sprite_extract(Tile.PIC_ICON[obj_what],20,1,0)
		else:
			#Others Object
			self.img_pattern ,self.img_pattern_rect = self.load_png(Tile.PIC_ICON[obj_what])
		
	def Sprite_extract(self, Sprite_sheet_filename, len_sprt_size, pos_cell_x, pos_cell_y):
		#len_sprt_size = Sprite size in Sprite_sheet_filname file

		#Sprite position in Sprite_sheet_filname file
		Pos_x = pos_cell_x*len_sprt_size
		Pos_y = pos_cell_y*len_sprt_size
		
		#Load the sprite sheet
		sprite_sheet,sprite_sheet_rect = self.load_png(Sprite_sheet_filename)

		#Locate the sprite in the sprite sheet - Rect(left, top, width, height) -> Rect
		sprite_sheet.set_clip(pygame.Rect(Pos_x, Pos_y, len_sprt_size, len_sprt_size))
		
		#Extract the sprite
		self.img_pattern = sprite_sheet.subsurface(sprite_sheet.get_clip())
		
		#Creation of the surface
		self.img_pattern_rect = self.img_pattern.get_rect()
	
	def load_png(self, name):
		#Load a picture from the repertory RESSOURCE and return a picture object
		fullname = os.path.join('./ressource/', name)
		img = pygame.image.load(fullname)
		
		if img.get_alpha is None:
			img = img.convert()
		else:
			img = img.convert_alpha()
		
		#Creation of the surface			
		return img, img.get_rect()

