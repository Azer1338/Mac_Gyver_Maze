# -*- coding: utf-8 -*-

import pygame
import map_generator


class Character(pygame.sprite.Sprite):
	#Creation of characters Mac Gyver and Guard
	
	def __init__(self, Who, Kind_of):
		#Load of the legacy from the library
		pygame.sprite.Sprite.__init__(self)

		#Load the picture
		if Kind_of == "Heroes" :
			#Motion of the Mac_Gyver icon
			self.image, self.image_rect = map_generator.load_png("./ressource/MacGyver.png")
		else:
			#Motion of the Guard icon
			self.image, self.image_rect = map_generator.load_png("./ressource/Gardien.png")
		
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.speed = Sprite_size
		#self.position='''
		pass
	'''	
	def update(self):
		pass
		#newpos= 
		
	
	def move_up(self):
		print("Up")
	
	def move_down(self):
		print("Down")
		
	def move_left(self):
		print("Left")
		
	def move_right(self):
		print("Right")
		'''
		
def create_actors():
	#images
	global jungle,jungle_rect
	
	jungle=pygame.image.load("./ressource/tile-crusader-logo.png")
	jungle=jungle.convert()
	
	jungle_rect=jungle.get_rect()
	
	#Mac Gyver icon
	global mac_gyver,mac_gyver_rect
	
	mac_gyver = pygame.image.load("./ressource/MacGyver.png")
	mac_gyver = mac_gyver.convert_alpha()
	
	mac_gyver_rect=mac_gyver.get_rect()
	
	mac_gyver_rect.center=((200,200))
	
	#Guard icon
	global guard,guard_rect
	
	guard = pygame.image.load("./ressource/Gardien.png")
	guard = guard.convert_alpha()
	
	guard_rect=guard.get_rect()
	
	guard_rect.bottom=height_screen


def action_event(event):
	#Keyboard pressed
	if event.type==pygame.KEYDOWN:
		if event.key == pygame.K_SPACE:
			print("Down")
			sound.play()
	
	#Keyboard released
	if event.type==pygame.KEYUP:
		if event.key == pygame.K_SPACE:
			print("Up")
			music.play()


def action_update (loc_delta):
	mac_gyver_rect.x += 2
	if mac_gyver_rect.left > width_screen:
		mac_gyver_rect.left=0


def action_render (loc_screen):
	#Surface management
	#background
	loc_screen.blit(jungle,jungle_rect)
	#Guard icon
	loc_screen.blit(guard,guard_rect)
	#Mac gyver icon
	loc_screen.blit(mac_gyver,mac_gyver_rect)
	
	#Labels
	label=myfont.render("Point=0",1,color_green)
	loc_screen.blit(label,(10,10))
	
	#display the result
	pygame.display.flip()


	
if __name__ == '__main__':
	main()
