# -*- coding: utf-8 -*-

import pygame

import sound_management
import map_generator
import maze_generator
import label_generator
import actors_generator
import object_generator

from sys import exit


def Sound_generation():
	#Launch of the music sound
	pygame.mixer.init()
	sound_management.activation_music()
	#sound_management.activation_sound()
		
def update_screen(Screen_to_update,maze,character1,character2,object1,object2,object3,object4):
	#Update the screen with the position of the path
	Screen_to_update.update_background_screen(maze)
	
	#Update the screen with the position of Characters
	Screen_to_update.screen.blit(character1.character_icon,(character1.pos_x_char,character1.pos_y_char))
	Screen_to_update.screen.blit(character2.character_icon,(character2.pos_x_char,character2.pos_y_char))
	
	#Update the screen with the position of the object
	Screen_to_update.screen.blit(object1.object_icon,(object1.pos_x_obj,object1.pos_y_obj))
	Screen_to_update.screen.blit(object2.object_icon,(object2.pos_x_obj,object2.pos_y_obj))
	Screen_to_update.screen.blit(object3.object_icon,(object3.pos_x_obj,object3.pos_y_obj))
	Screen_to_update.screen.blit(object4.object_icon,(object4.pos_x_obj,object4.pos_y_obj))
	Screen_to_update.display_on_screen()
	pass
	
def main():
	
	#Sound Generation
	Sound_generation()
	
	#Map Generation
	First_screen = map_generator.Monitor()
	
	#Maze Generation
	maze_on_screen = maze_generator.Maze()
	
	#Player generation
	player_on_screen = actors_generator.Character("Mac_Gyver")
	guard_on_screen = actors_generator.Character("Gard")
	
	#Object Generation
	needle_on_screen = object_generator.Object("Needle")
	syringe_on_screen = object_generator.Object("Syringe")
	tube_on_screen = object_generator.Object("Tube")
	ether_on_screen = object_generator.Object("Ether")
	
	#Check if the object is on the path
	needle_on_screen.object_on_path(maze_on_screen.maze_matrix)
	syringe_on_screen.object_on_path(maze_on_screen.maze_matrix)
	tube_on_screen.object_on_path(maze_on_screen.maze_matrix)
	ether_on_screen.object_on_path(maze_on_screen.maze_matrix)
	
	#Infinity loop to catch the player moves and regenerate the maze
	infinity_loop = True
	
	#Launch the loop
	while infinity_loop == True:
		#update the screen
		update_screen(First_screen,maze_on_screen,player_on_screen,guard_on_screen,needle_on_screen,syringe_on_screen,tube_on_screen,ether_on_screen)
		
		#Exit screen 
		for evt in pygame.event.get():
			#Screen Exit - X on the top right of the screen
			if evt.type == pygame.QUIT:
				infinity_loop=False
			#Keyboard pressed
			if evt.type==pygame.KEYDOWN:
				if evt.key == pygame.K_ESCAPE:
					infinity_loop=False
				if evt.key == pygame.K_UP:
					player_on_screen.move_up()
				if evt.key == pygame.K_DOWN:
					player_on_screen.move_down()
				if evt.key == pygame.K_LEFT:
					player_on_screen.move_left()
				if evt.key == pygame.K_RIGHT:
					player_on_screen.move_right()
				if evt.key == pygame.K_SPACE:
					print("0")

	return 0
	

if __name__ == '__main__':
	main()
