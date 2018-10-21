# -*- coding: utf-8 -*-

def sound_music():
	#definition of the sound
	global sound
	sound=pygame.mixer.Sound("./ressource/0433.ogg")
	sound.set_volume(0.8)
	
	#definition of the music
	pygame.mixer.music.load("./ressource/0315.ogg")
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)


if __name__ == '__main__':
	main()
