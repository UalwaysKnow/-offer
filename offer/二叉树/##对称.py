class solution:
	def __init__(self,root):
		self.root = root
		self.left = root.left
		self.right = root.right
	def symm(self,left,right):
		if self.root == None:
			return
		if not left:
			return right == None
		if not right:
			return False
		if left.item != right.item:
			return False
		return (self.symm(left.left,right.right)) and (self.symm(left.right,right.left))