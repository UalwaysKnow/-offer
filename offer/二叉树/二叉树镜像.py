'''实质上是遍历问题'''
def method(root):
	if root == None:
		return False
	stack = []
	stack.append(root)
	while stack:
		currentNode = stack.pop(0)
		currentNode.left,currentNode.right = currentNode.right,currentNode.left
		if currentNode.right:
			stack.append(currentNode.right)
		if currentNode.left:
			stack.append(currentNode.left)

def digui(root):
	if root == None:
		return
	if root.left == None and root.left == None:
		return
	root.left,root.right = root.right,root.left
	digui(root.left)
	digui(root.right)
