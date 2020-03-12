def preOrder(self,root):
	if root == None:
		return None
	print(root.item)
	self.preOrder(root.left)
	self.preOrder(root.right)
def midOrder(self,root):
	if root == None:
		return None
	self.midOrder(root.left)
	print(root.item)
	self.midOrder(root.right)
def bacOrder(self,root):
	if root == None:
		return None
	print(root.item)
	self.midOrder(root.left)
	self.midOrder(root.right)