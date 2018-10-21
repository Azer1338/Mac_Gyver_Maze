# -*- coding: utf-8 -*-

import pygame

import sound_management
import map_generator
import maze_generator
import label_generator
import actors_generator

from sys import exit


def Sound_generation():
	#Launch of the music sound
	pygame.mixer.init()
	sound_management.activation_music()
	#sound_management.activation_sound()
		
def Character_generation(screen):
	#Player generation
	#player_on_screen = actors_generator.Character("Mac_Gyver")
	#screen.blit(player_on_screen.character_icon,(player_on_screen.pos_x_char,player_on_screen.pos_y_char))
	pass
	
def update_screen(Screen_to_update,character):
	Screen_to_update.update_background_screen()
	Screen_to_update.screen.blit(character.character_icon,(character.pos_x_char,character.pos_y_char))
	Screen_to_update.display_on_screen()
	pass
	
def main():
	
	#Sound Generation
	Sound_generation()
	
	#Map Generation
	First_screen = map_generator.Monitor()
	
	#Player generation
	player_on_screen = actors_generator.Character("Mac_Gyver")
	
	#Infinity loop to catch the player moves and regenerate the maze
	infinity_loop = True
	
	#Launch the loop
	while infinity_loop == True:
		#update the screen
		update_screen(First_screen,player_on_screen)
		
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
