# -*- coding: utf-8 -*-

import pygame


def label():
	# Definition of the font
	global myfont
	myfont = pygame.font.SysFont("comicsansms", 25)


def top_title_generation():
	# Definition of the main screen title
	pygame.display.set_caption("Mac Gyver Maze")
