# -*- coding: utf-8 -*-

import pygame
import os
import numpy

import Tile


class Screen_Monitor():

	# Class Attributes
	# Mesure of a Sprite
	SPRITE_SIZE = 43
	# Mesure of a side of the screen
	LENGTH_PER_SIDE = 15
	# Dimension of the screen
	WIDTH_SCREEN = SPRITE_SIZE*LENGTH_PER_SIDE
	HEIGHT_SCREEN = SPRITE_SIZE*LENGTH_PER_SIDE
	# Frame Per Screen
	FPS = 25

	# Dictonnary Number on maze - Obj
	OBJ_ICON =	{ 	0	:	"Path",
					1 	:	"Wall",
					2	:	"Needle",
					3	:	"Syringe",
					5	:	"Tube",
					7	:	"Ether",
					8	:	"Mac_Gyver",
					88	:	"Guard"
				}

	def __init__(self):
		# Attribute
		self.screen = None
		self.status_game = "On Going"

		# Initialisation of the pygame library
		pygame.init()

		# Creation of the gaming screen
		self.screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN))

		# Top title generation
		self.top_title_generation()

		# FPS initialisation
		self.fps_management_init()

	def top_title_generation(self):
		# Definition of the main screen title
		pygame.display.set_caption("Mac Gyver Maze")

	def fps_management_init(self):
		# FPS Management
		self.clock = pygame.time.Clock()

	def fps_management(self):
		# Check the FPS at every screen update
		self.clock.tick(Screen_Monitor.FPS)

	def load_matrix(self, matrix):
		# Initialise a proper maze_matrix for futures modifications
		self.screen_maze_matrix = [[0]*Screen_Monitor.LENGTH_PER_SIDE for i in range(Screen_Monitor.LENGTH_PER_SIDE)]
		# Copy paste initial maze_matrix to maze_matrix in order
		self.screen_maze_matrix_updated = [[0]*Screen_Monitor.LENGTH_PER_SIDE for i in range(Screen_Monitor.LENGTH_PER_SIDE)]

		# Replace number par OBJ_ICON name - minus 1 to respect the dimension of the table
		for i in range(0, Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0, Screen_Monitor.LENGTH_PER_SIDE):
				self.screen_maze_matrix[j][i] = Screen_Monitor.OBJ_ICON[matrix.maze_matrix[i][j]]
				self.screen_maze_matrix_updated[j][i] = Screen_Monitor.OBJ_ICON[matrix.maze_matrix[i][j]]

		# Display on screen
		pygame.display.flip()

	def initialise_screen(self):
		# Generate and display all background tiles + Characters
		for i in range(0, Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0, Screen_Monitor.LENGTH_PER_SIDE):
				self.draw(Tile.Tile(self.screen_maze_matrix[j][i]), j, i)

		# Display on screen
		pygame.display.flip()

	def update_screen(self):
		# FPS management
		self.fps_management_init()

		# Compare every tiles in order to determine which one was modified
		for i in range(0, Screen_Monitor.LENGTH_PER_SIDE):
			for j in range(0, Screen_Monitor.LENGTH_PER_SIDE):
				if self.screen_maze_matrix[j][i] != self.screen_maze_matrix_updated[j][i]:
					self.draw(Tile.Tile(self.screen_maze_matrix_updated[j][i]), j, i)

				# Upload the matrix reference
				self.screen_maze_matrix[j][i] = self.screen_maze_matrix_updated[j][i]

		# Display on screen
		pygame.display.flip()

	def draw(self, object_to_draw, pos_x_in_matrix, pos_y_in_matrix):

		# Load the pattern to draw
		pattern = object_to_draw.img_pattern
		pattern = pygame.transform.scale(pattern, (Screen_Monitor.SPRITE_SIZE, Screen_Monitor.SPRITE_SIZE))

		# Add a image of the object on the cell (pos_x, pos_y)
		self.screen.blit(pattern, (pos_x_in_matrix*Screen_Monitor.SPRITE_SIZE, pos_y_in_matrix*Screen_Monitor.SPRITE_SIZE))

	def display_backpack(self, character):
		# Create a new screen
		self.screen_backpack = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN))

		# Fill the screen with a single color
		self.screen_backpack.fill((100, 110, 150))

		# Write the player s backpack content
		font = pygame.font.Font(None, 24)
		backpack_character = font.render(str(numpy.array(character.backpack)), 1, (255, 255, 255))
		self.screen_backpack.blit(backpack_character, (300, 300))

		# Let the screen visible during few seconds
		pygame.display.flip()

		pygame.time.delay(1000)

		self.initialise_screen()

	def ending_display(self):
		# Create a new screen
		self.ending_screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN))

		# Fill the screen with a single color
		self.ending_screen.fill((100, 0, 150))

		# Write the player s backpack content
		font = pygame.font.Font(None, 24)
		Game_over_title = font.render("GAME-OVER", 1, (255, 255, 255))
		self.ending_screen.blit(Game_over_title, (self.WIDTH_SCREEN / 2 - 75, self.HEIGHT_SCREEN / 2))

		# Display the VICTORY or LOSER player's status
		ending_title = font.render(str(self.status_game), 1, (255, 255, 255))

		self.ending_screen.blit(ending_title, (self.WIDTH_SCREEN/2 - 50, self.HEIGHT_SCREEN/2 + 100))

		# Let the screen visible during few seconds
		pygame.display.flip()
		pygame.time.delay(3000)
