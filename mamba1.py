import pygame
import sys
import time

SKY = (120, 200, 250)

def main():
	print("hello game world")
	
	# Initialize Game display
	pygame.init()
	size = width, height = 600, 400
	screen = pygame.display.set_mode(size)
	
	screen.fill(SKY)
	
	Player = pygame.Rect(200,200,50,100)
	
	pygame.draw.rect(screen,(255,0,0),Player)
	
	pygame.display.flip()
	
	time.sleep(5)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	

if __name__ == "__main__":
	main()
