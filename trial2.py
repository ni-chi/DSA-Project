import os, sys
import pygame

class Character :
	def __init__(self, rect) :
		self.rect = pygame.Rect(rect)
		self.click = False
		self.image = pygame.Surface(self.rect.size)
		self.image.fill((255, 0, 0))
		self.text = 'NO'

	def update(self, surface) :
		if self.click :
			self.rect.center = pygame.mouse.get_pos()
		x = self.rect.topleft
		y = self.rect.bottomright
		a = [list(x), list(y)]
		surface.blit(self.image, self.rect)
		return a

	def game_event_loop(self, Player1, Player2) :
		for event in pygame.event.get() :
			if event.type == pygame.MOUSEBUTTONDOWN :
				if Player1.rect.collidepoint(event.pos) :
					Player1.click = True
				if Player2.rect.collidepoint(event.pos) :
					Player2.click = True
			elif event.type == pygame.MOUSEBUTTONUP :
				Player1.click = False
				Player2.click = False
			elif event.type == pygame.QUIT or event.type == pygame.K_ESCAPE :
				pygame.quit()
				sys.exit()


def main() :
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	font = pygame.font.SysFont('Comic Sans MS', 30)
	Surface = pygame.display.set_mode((1000, 600))
	MyClock = pygame.time.Clock()
	Player = Character((0, 0, 10, 150))
	Player.rect.center = Surface.get_rect().center
	while True :
		white = (255, 255, 255)
		blue = (0, 0, 255)
		game_event_loop(Player)
		Surface.fill(white)
		pygame.draw.rect(Surface,blue,(200,150,100,50))
		t = Player.update(Surface)
		textsurface = font.render(str(t), False, (0, 0, 0))
		Surface.blit(textsurface, (0, 0))
		pygame.display.update()
		MyClock.tick(60)




if __name__ == '__main__':
	main()