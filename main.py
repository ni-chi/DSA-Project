from trial2 import Character
import os, sys
import pygame


class ITNode:
	def __init__(self,a,b,n):
		self.label=n
		self.parent=None
		self.low = a
		self.high = b
		self.max = 0
		self.leftChild = None
		self.rightChild = None


class IntervalTree:

	def __init__(self):
		self.root=None


	def search(self,x,i):
		if self.root==None or x==None:
			return None
		if i[0]==x.low and i[1]==x.high:
			return x
		if i[0]<x.low:
			return self.search(x.leftChild,i)
		else:
			return self.search(x.rightChild,i)


	def maximum(self,x):
		while x.rightChild!=None:
			x=x.rightChild
		return x

	
	def predecessor(self,i):
		x=self.search(self.root,i)
		if x==None:
			return None
		if x.leftChild!=None:
			return self.maximum(x.leftChild)
		y=x.parent
		while y!=None and x!=y.rightChild:
			x=y
			y=y.parent
		if y==None:
			return None
		else:
			return y

	def doOverlap(self,i1,i2) :
		if i1[0] <= i2[1] and i2[0] <=i1[1] :
			return True
		return False


	def overlapSearch(self,root, i,o) :
		if root == None :
			return
		if self.doOverlap([root.low,root.high],i) :
			o.append(root.label)
		self.overlapSearch(root.leftChild, i,o)
		self.overlapSearch(root.rightChild,i,o)
		return o

	def height(self,z):
		hl=hr=0
		if z==None:
			return 0
		if z.leftChild==None and z.rightChild==None:
			return 1
		else:
			if z.leftChild!=None:
				hl=self.height(z.leftChild)
			if z.rightChild!=None:
				hr=self.height(z.rightChild)
		if hl>=hr:
			return hl+1
		else:
			return hr+1

	def updateMax(self,x):
		a=0
		b=0
		if x.leftChild!=None:
			self.updateMax(x.leftChild)
			a=x.leftChild.max
		if x.rightChild!=None:
			self.updateMax(x.rightChild)
			b=x.rightChild.max
		if a>b:
			x.max=a
		else:
			x.max=b
		if x.high>x.max:
			x.max=x.high


	def insert(self,root, x=None) :
		if self.root == None :
			self.root=x
			
		else:
			l = root.low

			if x.low < l :
				if root.leftChild==None:
					root.leftChild=x
					x.parent=root
				else:
					self.insert(root.leftChild,x)
			else :
				if root.rightChild==None:
					root.rightChild=x
					x.parent=root
				else:
					self.insert(root.rightChild,x)

		self.compare(x)
		
		
		
		
	def compare(self,z):
		while z!=None:
			hl=self.height(z.leftChild)
			hr=self.height(z.rightChild)
			if abs(hl-hr)<=1:
				z=z.parent
			elif hl>=hr:
				y=z.leftChild
				h1=self.height(y.leftChild)
				h2=self.height(y.rightChild)
				if h1>=h2:							#Case 1
					self.rotateright(y,z)
					z=y.parent

				else:								#Case 3
					x=y.rightChild
					self.rotateleft(x,y)
					self.rotateright(x,z)
					z=x.parent

			else:
				y=z.rightChild
				h1=self.height(y.leftChild)
				h2=self.height(y.rightChild)
				if h1<=h2:							#Case 2
					self.rotateleft(y,z)
					z=y.parent

				else:								#Case 4
					x=y.leftChild
					self.rotateright(x,y)
					self.rotateleft(x,z)
					z=x.parent
		while self.root.parent!=None:
			self.root=self.root.parent
			self.compare(z)
				
	def rotateleft(self,y,z):
		z.rightChild=y.leftChild
		if y.leftChild!=None:
			y.leftChild.parent=z
		y.leftChild=z
		y.parent=z.parent
		if z.parent!=None:
			if z.parent.rightChild==z:
				z.parent.rightChild=y
			else:
				z.parent.leftChild=y
		z.parent=y

	def rotateright(self,y,z):
		z.leftChild=y.rightChild
		if y.rightChild!=None:
			y.rightChild.parent=z
		y.rightChild=z
		y.parent=z.parent
		if z.parent!=None:
			if z.parent.rightChild==z:
				z.parent.rightChild=y
			else:
				z.parent.leftChild=y
		z.parent=y
		

	def delete(self,i):
		x=self.search(self.root,i)
		if x.leftChild==None and x.rightChild==None:
			y=x.parent
			z=y
			if y.leftChild==x:
				y.leftChild=None
			else:
				y.rightChild=None
		else:
			if x.leftChild==None:
				if x.parent.leftChild==x:
					x.parent.leftChild=x.rightChild
				else:
					x.parent.rightChild=x.rightChild
				x.rightChild.parent=x.parent
			elif x.rightChild==None:
				if x.parent.leftChild==x:
					x.parent.leftChild=x.leftChild
				else:
					x.parent.rightChild=x.leftChild
				x.leftChild.parent=x.parent
			else:
				y=self.predecessor([x.low,x.high])
				self.delete([y.low,y.high])
				x.low=y.low
				x.high=y.high
			z=x
		self.compare(z)
		self.updateMax(self.root)

	def inorder(self,root) :
		if root == None :
			return root

		self.inorder(root.leftChild)
		print("[" + str(root.low) + ", " + str(root.high) + "]" + "max = " + str(root.max))
		self.inorder(root.rightChild)

	def preorder(self,root) :
		if root == None :
			return root

		print("[" + str(root.low) + ", " + str(root.high) + "]" + "max = " + str(root.max))
		self.preorder(root.leftChild)
		self.preorder(root.rightChild)


class GUI :
	def __init__(self) :
		self.white = (255, 255, 255)
		self.blue = (0, 0, 255)
		self.Player1 = Character((0, 0, 3, 150))
		self.Player2 = Character((0, 0, 150, 3))
		self.Surface = pygame.display.set_mode((1000, 600))
		self.MyClock = pygame.time.Clock()


	def initial(self) :
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()
		self.Player1.rect.center = self.Surface.get_rect().center
		self.Player2.rect.center = self.Surface.get_rect().center
		self.font = pygame.font.SysFont('Comic Sans MS', 30)

	def loop(self, tx,ty) :
		self.Player2.game_event_loop(self.Player2, self.Player1)
		self.Surface.fill(self.white)
		rect = pygame.Rect(200, 150, 100, 50)
		image = pygame.Surface(rect.size)
		image.fill((0, 0, 255))
		self.Surface.blit(image, rect)
		rect = pygame.Rect(400, 150, 100, 50) #(x coordinate, y coordinate, x size, y size)
		image = pygame.Surface(rect.size)
		image.fill((0, 255, 255))
		self.Surface.blit(image, rect)
		rect = pygame.Rect(400, 250, 100, 50) #(x coordinate, y coordinate, x size, y size)
		image = pygame.Surface(rect.size)
		image.fill((255, 255, 0))
		self.Surface.blit(image, rect)
		rect = pygame.Rect(200, 250, 100, 50) #(x coordinate, y coordinate, x size, y size)
		image = pygame.Surface(rect.size)
		image.fill((0, 255, 0))
		self.Surface.blit(image, rect)
		t1 = self.Player1.update(self.Surface)
		t2 = self.Player2.update(self.Surface)
		
		# x=[]
		# y=[]
		x=tx.overlapSearch(tx.root,[t1[0][0],t1[1][0]],[])
		y=ty.overlapSearch(ty.root,[t1[0][1],t1[1][1]],[])
		for i in x:
			for j in y:
				if i==j:
					self.Player1.text='YES'
				else:
					self.Player1.text='NO'

		x=tx.overlapSearch(tx.root,[t2[0][0],t2[1][0]],[])
		y=ty.overlapSearch(ty.root,[t2[0][1],t2[1][1]],[])
		for i in x:
			for j in y:
				if i==j:
					self.Player1.text='YES'
				else:
					self.Player1.text='NO'
		
		answer = self.font.render(self.Player1.text, False, (0, 255, 0))
		self.Surface.blit(answer, (500, 100))
		self.Player1.text = 'NO'
		textsurface = self.font.render(str(t2), False, (0, 100, 0))
		self.Surface.blit(textsurface, (0, 0))

	
def main() :
	pg = GUI()
	pg.initial()

	ex = [[200, 300], [400, 500]]
	ey=[[150,200], [250, 300]]
	tx = IntervalTree()
	ty = IntervalTree()
	for j in ex:
		tx.insert(tx.root,ITNode(j[0], j[1],'A'))
	for j in ey:
		ty.insert(ty.root,ITNode(j[0], j[1],'A'))
	tx.updateMax(tx.root)
	ty.updateMax(ty.root)
	tx.inorder(tx.root)
	ty.inorder(ty.root)
	print(tx.root.low,tx.root.high)
	print(ty.root.low,ty.root.high)
	tx.preorder(tx.root)
	ty.preorder(ty.root)

	# l = t.overlapSearch(t.root,[1,100])
	# print l


	while True :
		pg.loop(tx,ty)
		pygame.display.update()
		pg.MyClock.tick(60)

if __name__ == '__main__':
	main()