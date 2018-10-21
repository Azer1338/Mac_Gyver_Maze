# -*- coding: utf-8 -*-

import pygame

import sound_management
import map_generator
import label_generator
import actors_generator

from sys import exit


def Sound_generation():
	#Launch of the music sound
	pygame.mixer.init()
	sound_management.activation_music()
	#sound_management.activation_sound()


def Map_generation():
	#Creation of the screen
	First_screen = map_generator.Monitor()
	
	#Creation of the map
	First_screen.map_init()


def Character_generation():
	#Initialisation of the player
	player = actors_generator.Character("Mac_Gyver","Heroes")
	#final_Guard = actors_generator.Character("Guard","Vilain")
	
def main():
	
	#Sound Generation
	Sound_generation()
	
	#Map Generation
	Map_generation()
	
	#Characters Generation 
	#Character_generation()
	
	#Infinity loop to catch the player moves
	#Creation of the inifinity loop
	infinity_loop = True
	
	while infinity_loop == True:
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
					player.move_up()
				if evt.key == pygame.K_DOWN:
					player.move_down()
				if evt.key == pygame.K_LEFT:
					player.move_left()
				if evt.key == pygame.K_RIGHT:
					player.move_right()
				if evt.key == pygame.K_SPACE:
					print("0")

	return 0
	

if __name__ == '__main__':
	main()
