# -*- coding: utf-8 -*-

import numpy


class Maze():
	# Create a Maze from a txt file

	def __init__(self):

		# Attributes
		# Array [] [] Maze matrix form
		self.maze_matrix = []

		# Open the maze matrix file
		self.upload_maze_matrix_txt_file()

	def upload_maze_matrix_txt_file(self):

		# Open the Maze.txt file
		fichier = open("Maze.txt", "r")

		# Create a array from the file
		self.maze_matrix = numpy.genfromtxt("Maze.txt", delimiter=',', dtype=int)

		# Close the file to save CPU
		fichier.close()
		
		print(self.maze_matrix)
