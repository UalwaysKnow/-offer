def preOrder(self,root):
	if root == None:
		return
	stack = []
	result = []
	node = root
	while node or stack:
		while node:
			result.append(node.val)
			stack.append(node)
			node = node.left
		node = stack.pop()
		node = node.right
	return result
def midOrder(self,root):
	if root == None:
		return
	stack = []
	result = []
	node = root
	while stack or node:
		while node:
			stack.append(node)
			node = node.left
		node = stack.pop()
		result.append(node.item)
		node = node.right
def bacOrder(self,root):
	if root == None:
		return
	stack = []
	result = []
	node = root
	while node or stack:
		while node:
			result.insert(0,node)
			stack.append(node)
			node = node.right
		node = stack.pop()
		node = node.left