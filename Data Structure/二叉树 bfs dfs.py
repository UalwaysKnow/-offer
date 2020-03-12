'''
DFS效果和先序遍历一样，使用栈实现
BFS即层次遍历，使用队列实现
'''
def bfs(self,root):
	if root == None:
		return None
	queue = []
	queue.append(root)
	while queue:
		currentNode = queue.pop(0)
		print(currentNode.item)
		if currentNode.left is not None:
			queue.append(currentNode.left)
		if currentNode.right is not None:
			queue.append(currentNode.right)

def dfs(self,root):
	if root == None:
		return None
	stack = []
	stack.append(root)
	while stack:
		currentNode = stack.pop()
		print(currentNode.item)
		if currentNode.right:
			stack.append(currentNode.right)
		else:
			stack.append(currentNode.left)
