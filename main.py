class ITNode :
	def __init__(self, a = None, b = None) :
		self.parent=None
		self.low = a
		self.high = b
		self.max = 0
		self.leftChild = None
		self.rightChild = None


class IntervalTree :
	def __init__(self, t = None) :
		self.root = t

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

		if x.max < x.high :
			x.max = x.high
			self.updateMax(x)

	def updateMax(self,x):
		p=x.parent
		while p!=None:
			if p.max<x.max:
				p.max=x.max
			p=p.parent

	def doOverlap(self,i1,i2) :
		if i1[0] <= i2[1] and i2[0] <=i1[1] :
			return True
		return False


	def overlapSearch(self,root, i) :
		if root == None :
			return None
		if self.doOverlap([root.low,root.high],i) :
			return [root.low,root.high]
		if root.leftChild != None and root.leftChild.max >= i[0] :
			return self.overlapSearch(root.leftChild, i)

		return self.overlapSearch(root.rightChild,i)



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


def main() :
	e = [[15, 20], [10, 30], [17, 19],[5, 20], [12, 15], [30, 40]]
	rat = IntervalTree()
	for j in e :
		rat.insert(rat.root,ITNode(j[0], j[1]))
	rat.inorder(rat.root)
	print(rat.root.low,rat.root.high)
	rat.preorder(rat.root)
	print(rat.overlapSearch(rat.root,[6,7]))

if __name__ == '__main__':
	main()