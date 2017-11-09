class ITNode :
	def __init__(self, a = None, b = None) :
		self.parent=None
		self.low = a
		self.high = b
		self.max = 0
		self.left = None
		self.right = None

class IntervalTree :
	def __init__(self, t = None) :
		self.root = t

	def insert(self,root, x=None) :
		if self.root == None :
			self.root=x
			
		else:
			l = root.low

			if x.low < l :
				if root.left==None:
					root.left=x
					x.parent=root
				else:
					self.insert(root.left,x)
			else :
				if root.right==None:
					root.right=x
					x.parent=root
				else:
					self.insert(root.right,x)

		if x.max < x.high :
			x.max = x.high
			self.updateMax(x)

	def updateMax(self,x):
		p=x.parent
		while p!=None:
			if p.max<x.max:
				p.max=x.max
			p=p.parent

	def doOverlap(self,i1, i2) :
		if i1.low <= i2.high and i2.low <=i1.high :
			return True
		return False


	def overlapSearch(self,root, i) :
		if root == None :
			return None
		if self.doOverlap(root.i, i) :
			return root.i
		if root.left != None and root.left.max >= i.low :
			return self.overlapSearch(root.left, i)

		return self.overlapSearch(root.right, i)


	def inorder(self,root) :
		if root == None :
			return root

		self.inorder(root.left)
		print("[" + str(root.low) + ", " + str(root.high) + "]" + "max = " + str(root.max))
		self.inorder(root.right)

	def preorder(self,root) :
		if root == None :
			return root

		print("[" + str(root.low) + ", " + str(root.high) + "]" + "max = " + str(root.max))
		self.preorder(root.left)
		self.preorder(root.right)


def main() :
	e = [[15, 20], [10, 30], [17, 19],[5, 20], [12, 15], [30, 40]]
	a = []
	rat = IntervalTree()
	for j in e :
		a.append(ITNode(j[0], j[1]))
	for i in a:
		rat.insert(rat.root,i)
	rat.inorder(rat.root)
	print(rat.root.low,rat.root.high)
	rat.preorder(rat.root)

if __name__ == '__main__':
	main()