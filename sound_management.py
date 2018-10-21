# -*- coding: utf-8 -*-

import pygame

def activation_music():
	pygame.mixer.music.load("./ressource/0315.ogg")
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)
	
def desactivation_music():
	pygame.mixer.music.stop()
	
def activation_sound():
	sound=pygame.mixer.Sound("./ressource/0433.ogg")
	sound.play(0)


def main():
	pygame.mixer.init()

if __name__ == '__main__':
	main()
