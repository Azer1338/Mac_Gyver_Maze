# -*- coding: utf-8 -*-

import pygame

import sound_generator
import screen_generator
import path_generator
import object_generator
'''
import character_generator

'''

from sys import exit
	
def main():
	
	#Generation of a background music
	Music = sound_generator.Music_Sound()
	Music.background_music("ON")
	
	#Generation of a sound
	Sound_drum = sound_generator.Music_Sound()
	Sound_drum.BomBomBom()
	
	#Generation of the Game screen
	Game_screen = screen_generator.Screen_Monitor()
	
	#Generation of the path (maze)
	Maze_path = path_generator.Maze_builder()
	Game_screen.draw_path(Maze_path)
	
	#Generation of the object to pick up
	Needle = object_generator.Object_builder("Needle")
	Tube = object_generator.Object_builder("Tube")
	Ether = object_generator.Object_builder("Ether")
	#Generation of a 
	
	'''
	#Generation of the actors
	Mac_gyver = character_generator.Player()
	Guard = character_generator.Player()
	
	#
	
	
	
	
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
	
	'''
	#Infinity loop to catch the player moves and regenerate the maze
	infinity_loop = True
	
	#TEST
	Mur=pygame.Rect((0,0),(1,1))
	
	#Launch the loop
	while infinity_loop == True:
		#update the screen
		pygame.display.flip()
		#update_screen(First_screen,maze_on_screen,player_on_screen,guard_on_screen,needle_on_screen,syringe_on_screen,tube_on_screen,ether_on_screen)
		
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
