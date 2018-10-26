# -*- coding: utf-8 -*-

import pygame
from sys import exit

import Music_Sound
import Screen_Monitor
import Maze
import Object
import Player

	
def main():
	
	#Generation of a background music
	Music = Music_Sound.Music_Sound()
	Music.background_music("ON")
	
	#Generation of a sound
	Sound_drum = Music_Sound.Music_Sound()
	#Sound_drum.BomBomBom()
	
	#Generation of the Game screen
	Game_screen = Screen_Monitor.Screen_Monitor()
	
	#Generation of the path (maze)
	Maze_path = Maze.Maze(Game_screen)
	#Load the inital maze in the Screen
	Game_screen.load_matrix(Maze_path)
	
	#Generation of the object to pick up
	Needle = Object.Object("Needle",Game_screen)
	Tube = Object.Object("Tube",Game_screen)
	Ether = Object.Object("Ether",Game_screen)
	
	#Generation of the actors
	Mac_Gyver = Player.Player("Mac_Gyver",Game_screen)
	Guard = Player.Player("Guard",Game_screen)
	
	#Initialize the screen
	Game_screen.initalise_screen()
	
	#Infinity loop to catch the player moves and regenerate the maze
	infinity_loop = True
	
	#Launch the loop
	while infinity_loop == True:
		#update the screen
		Game_screen.fps_management()
		
		#Exit screen 
		for evt in pygame.event.get():
			#Screen Exit - X on the top right of the screen
			if evt.type == pygame.QUIT:
				infinity_loop=False
			#Keyboard pressed
			if evt.type==pygame.KEYDOWN:
				if evt.key == pygame.K_ESCAPE:
					infinity_loop=False
				#Move on screen
				if evt.key == pygame.K_UP:
					Mac_Gyver.move_up(Game_screen)
				if evt.key == pygame.K_DOWN:
					Mac_Gyver.move_down(Game_screen)
				if evt.key == pygame.K_LEFT:
					Mac_Gyver.move_left(Game_screen)
				if evt.key == pygame.K_RIGHT:
					Mac_Gyver.move_right(Game_screen)
				if evt.key == pygame.K_SPACE:
					print("0")
				Game_screen.update_screen()

	return 0
	
if __name__ == '__main__':
	main()
