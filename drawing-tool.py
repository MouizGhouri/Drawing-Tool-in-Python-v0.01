import pygame

def main () :

	pygame.init ()
	pygame.display.set_caption ("Drawing Tool v0.1 by Mouiz Ghouri (King_ftw)")

	running = True
	lmb_state = False
	last_pixel = {'x': -1, 'y': -1}

	screen = pygame.display.set_mode ((500, 500))
	screen.fill ((255, 255, 255))

	def drawPixel (mouse_position, last_x, last_y) :

		if last_x != -1 :

			x1, y1 = last_x, last_y

			pygame.draw.line (screen, (50, 50, 50), (x1, y1), mouse_position, 5)

		x, y = mouse_position
		last_pixel ['x'] = x
		last_pixel ['y'] = y
		pygame.draw.rect (screen, (50, 50, 50), (x, y, 1, 1))

	while running :

		for event in pygame.event.get () :

			pygame.display.update()

			if event.type == pygame.QUIT :
				running = False

			if event.type == 4 :
				if lmb_state == True:
					drawPixel (pygame.mouse.get_pos (), last_pixel ['x'], last_pixel ['y'])

			if event.type == 5 : 
				lmb_state = True

			elif event.type == 6 : 
				lmb_state = False

				last_pixel ['x'] = -1
				last_pixel ['y'] = -1

if __name__ == "__main__" :

	main ()
