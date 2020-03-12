'''输入两棵二叉树A，B，判断B是不是A的子树'''
# 考点一 判断是否为子树
def Issametree(rootA,rootB):
	if rootA is None and rootB is not None:
		return False
	elif rootA is not None and rootB is None:
		return False
	elif rootA is None and rootB is None:
		return True

	if rootA.value == rootB.value:
		return Issametree(rootA.left,rootB.left) and Issametree(rootA.right,rootB.right)

def Issun(root1,root2):
	stack = []
	node = root1
	while stack or node:
		while node:
			if node == root2:
				if Issametree(node,root1):
					return True
			stack.append(node)
			node = node.left
		node = stack.pop()
		node = node.right
	return False
