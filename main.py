# -*- coding: utf-8 -*-

import pygame
from sys import exit

import Music_Sound
import Screen_Monitor
import Maze
import Object
import Character

	
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
	Maze_path = Maze.Maze()
	#Load the inital maze in the Screen
	Game_screen.load_matrix(Maze_path)

	#Generation of the object to pick up
	Needle = Object.Object("Needle",Game_screen)
	Tube = Object.Object("Tube",Game_screen)
	Ether = Object.Object("Ether",Game_screen)
	
	#Generation of the Characters
	Mac_Gyver = Character.Character("Mac_Gyver",Game_screen)
	Guard = Character.Character("Guard",Game_screen)

	#Initialize the screen
	Game_screen.initialise_screen()
	
	#Infinity loop to catch the player moves and regenerate the maze
	infinity_loop = True
	
	#Launch the loop
	while infinity_loop == True:
		
		#Exit screen 
		for evt in pygame.event.get():
			
			#Screen Exit - X on the top right of the screen
			if evt.type == pygame.QUIT:
				infinity_loop=False
				
			#Keyboard pressed
			if evt.type==pygame.KEYDOWN:
				# ESC key - Exit
				if evt.key == pygame.K_ESCAPE:
					infinity_loop=False
					
				#Player moves
				if evt.key == pygame.K_UP:
					Mac_Gyver.move_up()
				if evt.key == pygame.K_DOWN:
					Mac_Gyver.move_down()
				if evt.key == pygame.K_LEFT:
					Mac_Gyver.move_left()
				if evt.key == pygame.K_RIGHT:
					Mac_Gyver.move_right()
				
				#Backpack display
				if evt.key == pygame.K_SPACE:
					Game_screen.display_backpack(Mac_Gyver)
		
		#Check if the game is finished
		if Game_screen.status_game != "On Going": 
			#Game over - Display the ending screen
			Game_screen.ending_display()
			infinity_loop = False
			
		else:
			#Keep going the screen updating
			Game_screen.update_screen()
			
	return 0
	
if __name__ == '__main__':
	main()
