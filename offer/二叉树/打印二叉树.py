'''从上往下打印出二叉树的每个节点，同层节点从左至右打印。'''
def bfs(root):
	if root == None:
		return None
	queue = []
	queue.append(root)
	while queue:
		currentNode = queue.pop(0)
		print(currentNode.item)
		if currentNode.left:
			queue.append(currentNode.left)
		if currentNode.right:
			queue.append(currentNode.right)