import pygame, sys

class Character :
	def __init__(self, img) :
		self.click = False
		self.image = pygame.image.load(img)
		self.rect = self.image.get_rect()
		self.text = 'NO'

	def update(self, surface) :
		if self.click :
			self.rect.center = pygame.mouse.get_pos()
		surface.blit(self.image, self.rect)
		return [self.rect.topleft, self.rect.bottomright]

	def game_event_loop(self, Player1) :
		for event in pygame.event.get() :
			if event.type == pygame.MOUSEBUTTONDOWN :
				for i in range(1, 10) :
					if Player1[i].rect.collidepoint(event.pos) :
						Player1[i].click = True
			elif event.type == pygame.MOUSEBUTTONUP :
				for i in range(1, 10) :	
					Player1[i].click = False
			elif event.type == pygame.QUIT or event.type == pygame.K_ESCAPE :
				pygame.quit()
				sys.exit()


def main() :
	pygame.init()
	font = pygame.font.SysFont('Comic Sans MS', 30)
	Surface = pygame.display.set_mode((1000, 600))
	MyClock = pygame.time.Clock()
	Player = [None]
	for i in range(1, 10) :
		Player.insert(i, Character('jerry-' + str(i) + '.jpeg'))
		(x, y) = Surface.get_rect().topleft
		Player[i].rect.center = (x + i*100, y + i*50)
	while True :
		white = (255, 255, 255)
		blue = (0, 0, 255)
		Surface.fill(white)
		for i in range(1, 10) :
			Player[i].game_event_loop(Player)
			t = Player[i].update(Surface)
			textsurface = font.render(str(t), False, (0, 0, 0))
			Surface.blit(textsurface, (0, i*50))
		pygame.display.update()
		MyClock.tick(60)


if __name__ == '__main__':
	main()