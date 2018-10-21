# -*- coding: utf-8 -*-

import pygame
import map_generator


class Character():
	
	def __init__(self, who):
		# Mac Gyver have a specific position on the screen
		self.speed=1*map_generator.Sprite_size
		if who=="Mac_Gyver":
			#Position
			self.pos_x_char =10*map_generator.Sprite_size
			self.pos_y_char =10*map_generator.Sprite_size
			#Icon
			self.character_icon,self.character_icon_rect = map_generator.load_png("MacGyver.png")
		else:
			#Position
			self.pos_x_char =0
			self.pos_y_char =0
			#Icon
			self.character_icon,self.character_icon_rect = map_generator.load_png("Gardien.png")
		
	def move_up(self):
		#Character move up on the screen
		print("Up")
		self.new_pos_y_char= self.pos_y_char - self.speed
		self.pos_y_char = stay_on_screen(self.pos_y_char,self.new_pos_y_char,self.speed)
	
	def move_down(self):
		#Character move down on the screen
		print("Down")
		self.new_pos_y_char= self.pos_y_char + self.speed
		self.pos_y_char = stay_on_screen(self.pos_y_char,self.new_pos_y_char,self.speed)
		
	def move_left(self):
		#Character move left on the screen
		print("Left")
		self.new_pos_x_char= self.pos_x_char - self.speed
		self.pos_x_char = stay_on_screen(self.pos_x_char,self.new_pos_x_char,self.speed)
		
	def move_right(self):
		#Character move right on the screen
		print("Right")		
		self.new_pos_x_char= self.pos_x_char + self.speed
		self.pos_x_char = stay_on_screen(self.pos_x_char,self.new_pos_x_char,self.speed)

def stay_on_screen(init_position, new_position,move):
	#Limit Character moves on negative axis
	if new_position > (map_generator.side_square_screen_mesure*map_generator.Sprite_size-map_generator.Sprite_size):
		position_into_screen = init_position
	#Limit Character moves on negative axis
	elif new_position < 0:
		position_into_screen = init_position
	else :
		position_into_screen = new_position
	
	return position_into_screen
	
def main():
	pass
	
if __name__ == '__main__':
	main()
