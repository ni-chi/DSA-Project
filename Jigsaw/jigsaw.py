import pygame, sys
from p1 import ITNode,IntervalTree

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
		return [list(self.rect.topleft), list(self.rect.bottomright)]

	def game_event_loop(self, Player1) :
		for event in pygame.event.get() :
			if event.type == pygame.MOUSEBUTTONDOWN :
				for i in range(0, 3) :
					for j in range(0,3):
						if Player1[i][j].rect.collidepoint(event.pos) :
							Player1[i][j].click = True
			elif event.type == pygame.MOUSEBUTTONUP :
				for i in range(0, 3) :
					for j in range(0, 3) :	
						Player1[i][j].click = False
			elif event.type == pygame.QUIT or event.type == pygame.K_ESCAPE :
				pygame.quit()
				sys.exit()


def main() :
	c=[['A','D','G'],['B','E','H'],['C','F','I']]
	T=[[False for i in range(3)] for i in range (3)]
	S=[[True for i in range(3)] for i in range (3)]
	ex = [[300, 484,0], [486, 668,1],[670,852,2]]
	ey = [[100, 244,0], [246, 388,1],[390,532,2]]
	tx = IntervalTree()
	ty = IntervalTree()
	for j in ex:
		tx.insert(tx.root,ITNode(j))
	for j in ey:
		ty.insert(ty.root,ITNode(j))
	pygame.init()
	font = pygame.font.SysFont('Impact', 30)
	Surface = pygame.display.set_mode((1000, 600))
	MyClock = pygame.time.Clock()
	Player = [[None for i in range(3)] for i in range (3)]
	i=1
	for j in range(0,3) :
		for k in range(0,3):
			Player[k][j]=(Character('jerry-' + str(i) + '.jpeg'))
			(x, y) = Surface.get_rect().topleft
			Player[k][j].rect.center = (x + i*100, y + i*50)
			i=i+1
	while True :
		Surface.fill((127,255,255))
		pygame.draw.rect(Surface, (255, 250, 205), (300, 100, 552, 432))
		pygame.draw.rect(Surface, (0, 0, 0), (484,100, 2, 432))
		pygame.draw.rect(Surface, (0, 0, 0), (668, 100, 2, 432))
		pygame.draw.rect(Surface, (0, 0, 0), (300, 244, 552, 2))
		pygame.draw.rect(Surface, (0, 0, 0), (300, 388, 552, 2))
		for i in range(0, 3) :
			for j in range(0,3):
				Player[i][j].game_event_loop(Player)
				t = Player[i][j].update(Surface)
				x=tx.overlapSearch(tx.root,[t[0][0],t[1][0]])
				y=ty.overlapSearch(ty.root,[t[0][1],t[1][1]])
				if x==i and y==j:
					T[i][j]=True
				else:
					T[i][j]=False
				print(T)
				if T==S:
					textsurface = font.render(str("Puzzle Solved!"), False, (0, 0, 0))
					Surface.blit(textsurface, (500 ,100 ))
		pygame.display.update()
		MyClock.tick(60)


if __name__ == '__main__':
	main()