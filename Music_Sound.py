# -*- coding: utf-8 -*-

import pygame

class Music_Sound():
	#Object to manage the background music and event sound
	
	def __init__(self):
		pygame.mixer.init()
		self.back_music = "./ressource/0315.ogg"
		self.sound1 = pygame.mixer.Sound("./ressource/0433.ogg")
		
	def background_music(self,activation):
		if activation == "ON":
			pygame.mixer.music.load(self.back_music)
			pygame.mixer.music.set_volume(0.5)
			pygame.mixer.music.play(-1)
		elif activation == "OFF":
			pygame.mixer.music.stop()
		else:
			print("Argument not correct")
			
	def BomBomBom(self):
		self.sound1.set_volume(0.8)
		self.sound1.play(0)
		
