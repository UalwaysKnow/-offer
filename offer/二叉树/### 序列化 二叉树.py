class solution:
	def serialize(self,root):
		if not root:
			return '#'
		return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
	def deserialize(self,data):
		list = data.split(',')
		return self.deserializeTree(list)
	def deserializeTree(self,list):
		if len(list)<=0:
			return None
		val = list.pop(0)
		root = None
		if val != '#':
			root = TreeNode(int(val))
			root.left = self.deserializeTree(list)
			root.right = self.deserializeTree(list)
		return root