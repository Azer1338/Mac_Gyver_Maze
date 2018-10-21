# -*- coding: utf-8 -*-

import pygame

import sound_management
import map_generator
import label_generator
import actors_generator


from sys import exit


def main():
	
	#Creation of the map
	First_screen=map_generator.Monitor()
	
	First_screen.init_monitor()

	return 0


if __name__ == '__main__':
	main()
