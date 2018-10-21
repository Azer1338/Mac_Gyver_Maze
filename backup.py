
def main():
	
	#Initialisation of pygame library
	init_pygame_custom()
	
	#Initialisation of the maze path
	init_maze()

	#Creation of the infinity loop
	infinity_loop=True
	
	#create_actors()  
	#label()
	#sound_music()
	
	#print("x={0}, y={1}, w={2},h={3}".format(box_rect.x,box_rect.y,box_rect.w,box_rect.w))

	#Launch the infinity loop
	while infinity_loop == True:
		
		#FPS management
		delta_ms=clock.tick(fps)
				
		#Exit screen management
		for evt in pygame.event.get():
			#Screen Exit - X on the top right of the screen
			if evt.type == pygame.QUIT:
				infinity_loop=False
			#Keyboard pressed
			if evt.type==pygame.KEYDOWN:
				if evt.key == pygame.K_ESCAPE:
					infinity_loop=False
					
			#Keyboard management
			action_event(evt)
		
		#Motion of the object	
		#action_update(delta_s)
		
		#Render of the motion
		#action_render(screen)

	#Wait a bit to show correctly the main screen - ms
	#pygame.time.delay(2000)

	#endinf of the pygame library
	pygame.quit()
	#quit Python from sys library
	exit()

	return 
