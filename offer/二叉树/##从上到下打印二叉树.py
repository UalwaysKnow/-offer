def method(root):
	if root is None:
		return
	result = [] #二维数组
	current_level = []
	current_level.append(root)
	while current_level:
		current_result = []
		next_level = []
		for node in current_level:
			current_result.append(node.item)
			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)
		current_level = next_level
		result.append(current_result)
	return result