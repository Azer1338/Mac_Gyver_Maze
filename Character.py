# -*- coding: utf-8 -*-

import pygame
import Music_Sound


class Character():
	# Class Attributes
	SPEED = 1

	def __init__(self, who, screen):

		# Initialisation
		self.perso = who
		self.screen_to_display = screen

		self.pos_x_matrix = 0
		self.pos_y_matrix = 0

		# Initialisation of the backpack
		self.backpack = []

		# Mesure of the matrix per side
		self.length_matrix = len(screen.screen_maze_matrix)

		# Initialisation of Character's position
		self.initialise_position_on_maze_matrix()

	def initialise_position_on_maze_matrix(self):
		# Initial position of the icon in the maze matrix
		# Retain the pos x & y of the character from the maze matrix
		for i in range(0, self.length_matrix):
			for j in range(0, self.length_matrix):
				if self.screen_to_display.screen_maze_matrix[j][i] == self.perso:
					# Position
					self.pos_x_matrix = j
					self.pos_y_matrix = i

		# Display the character on screen
		self.screen_to_display.screen_maze_matrix_updated[self.pos_x_matrix][self.pos_y_matrix] = self.perso

	def move_up(self):
		# Character move up on the screen
		move = self.pos_y_matrix - Character.SPEED

		# Event during walking on the way to go home
		self.action_on_motion("Y", move)

	def move_down(self):
		# Character move down on the screen
		move = self.pos_y_matrix + Character.SPEED

		# Event during walking on the way to go home
		self.action_on_motion("Y", move)

	def move_left(self):
		# Character move left on the screen
		move = self.pos_x_matrix - Character.SPEED

		# Event during walking on the way to go home
		self.action_on_motion("X", move)

	def move_right(self):
		# Character move right on the screen
		move = self.pos_x_matrix + Character.SPEED

		# Event during walking on the way to go home
		self.action_on_motion("X", move)

	def action_on_motion(self, axis, move_proposal):
		# On the next tile, the Character can find:
		# If Wall, the Character could go there. Stay on same tile
		if axis == "X":
			# Check if the character is still in the screen frame
			new_position = self.stay_in_frame(move_proposal, self.pos_x_matrix)
			self.check_next_tile(new_position, self.pos_y_matrix)

		elif axis == "Y":
			# Check if the character is still in the screen frame
			new_position = self.stay_in_frame(move_proposal, self.pos_y_matrix)
			self.check_next_tile(self.pos_x_matrix, new_position)

	def stay_in_frame(self, pos_proposal, init_pos):
		# Make sure that the position prpposed will be in the screen frame
		if pos_proposal >= self.length_matrix or pos_proposal < 0:
			pos_proposal = init_pos

		return pos_proposal

	def check_next_tile(self, Xpos_in_matrice, Ypos_in_matrice):

		if self.screen_to_display.screen_maze_matrix[Xpos_in_matrice][Ypos_in_matrice] == "Wall":
			# Characters goes back to the initial position
			Xpos_in_matrice = self.pos_x_matrix
			Ypos_in_matrice = self.pos_y_matrix

		else:
			# The character will change from initial position to the new one
			if self.screen_to_display.screen_maze_matrix[Xpos_in_matrice][Ypos_in_matrice] == "Path":
				# No action on Path tiles
				pass

			elif self.screen_to_display.screen_maze_matrix[Xpos_in_matrice][Ypos_in_matrice] == "Guard":
				# Status of the overall game changed - Backpack checked
				self.check_backpack_content()
				pass

			else:
				# On all other tiles - Add the object in the backpack
				self.add_backpack_content(self.screen_to_display.screen_maze_matrix[Xpos_in_matrice][Ypos_in_matrice])

			# Replace the actual tile by a path
			self.screen_to_display.screen_maze_matrix_updated[self.pos_x_matrix][self.pos_y_matrix] = "Path"

			# Swap the new position with actual position
			self.pos_x_matrix = Xpos_in_matrice
			self.pos_y_matrix = Ypos_in_matrice

			# Place the Character on the new position
			self.screen_to_display.screen_maze_matrix_updated[self.pos_x_matrix][self.pos_y_matrix] = self.perso
			
			print("X={},Y={}".format(self.pos_x_matrix, self.pos_y_matrix))

	def check_backpack_content(self):
		# Verify if 3 elements are in the characters' backpack
		# Send back the status of the game depending of the status
		if len(self.backpack) == 3:
			self.screen_to_display.status_game = "Victory"

		else:
			self.screen_to_display.status_game = "LOSER : At least 1 thing is missing"

	def add_backpack_content(self, obj):
		# Add an object in the backpack
		self.backpack.append(obj)

		# Make a sound to celebrate that!
		Drum = Music_Sound.Music_Sound()
		Drum.bombombom()
