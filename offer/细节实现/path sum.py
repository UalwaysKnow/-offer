'''给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。'''
def path_sum(root,s):
	# 利用先序遍历解决
	if root == None:
		return
	stack = []
	result = []
	node = root
	while node or stack:
		while node:
			result.append(node.item)
			stack.append(node)
			node = node.left
		if node.left == None and node.right == None:
			if sum(result) == s:
				return True
		node = stack.pop()
		node = node.right
	return False