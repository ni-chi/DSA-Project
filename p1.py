class ITNode:
	def __init__(self,a,b):
		self.parent=None
		self.low = a
		self.high = b
		self.max = 0
		self.leftChild = None
		self.rightChild = None


class IntervalTree:

	def __init__(self):
		self.root=None


	def search(self,k,x):
		if self.root==None or x==None:
			return None
		if k==x.key:
			return x
		if k<x.key:
			return self.search(k,x.leftChild)
		else:
			return self.search(k,x.rightChild)

	def minimum(self,x):
		while x.leftChild!=None:
			x=x.leftChild
		return x

	def maximum(self,x):
		while x.rightChild!=None:
			x=x.rightChild
		return x

	def successor(self,k):
		x=self.search(k,self.root)
		if x.rightChild!=None:
			return self.minimum(x.rightChild)
		y=x.parent
		while y!=None and x!=y.leftChild:
			x=y
			y=y.parent
		if y==None:
			return None
		else:
			return y

	def predecessor(self,k):
		x=self.search(k,self.root)
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
		p=x.parent
		while p!=None:
			if p.max<x.max:
				p.max=x.max
			p=p.parent

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
					root.righChildt=x
					x.parent=root
				else:
					self.insert(root.rightChild,x)
		if x.max < x.high :
			x.max = x.high
			self.updateMax(x)
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
					rotateright(y,z)
					z=y.parent

				else:								#Case 3
					x=y.rightChild
					rotateleft(x,y)
					rotateright(x,z)
					z=x.parent

			else:
				y=z.rightChild
				h1=self.height(y.leftChild)
				h2=self.height(y.rightChild)
				if h1<=h2:							#Case 2
					rotateleft(y,z)
					z=y.parent

				else:								#Case 4
					x=y.leftChild
					rotateright(x,y)
					rotateleft(x,z)
					z=x.parent
		while self.root.parent!=None:
			self.root=self.root.parent
			self.compare(z)
				
		

	def delete(self,k):
		x=self.search(k,self.root)
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
				y=self.predecessor(x.key)
				self.delete(y.key)
				x.key=y.key
			z=x
		self.compare(z)

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



	
def rotateleft(y,z):
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

def rotateright(y,z):
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

	
def main():
	e = [[15, 20], [10, 30], [17, 19],[5, 20], [12, 15], [30, 40],[4,10],[2,5] ]
	rat = IntervalTree()
	for j in e :
		rat.insert(rat.root,ITNode(j[0], j[1]))
	rat.inorder(rat.root)
	print(rat.root.low,rat.root.high)
	rat.preorder(rat.root)


main()
