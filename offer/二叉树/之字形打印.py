def method(root):
	if root == None:
		return []
	result = []
	current_level = [root]
	i = 1
	while current_level:
		current_result = []
		next_level = []
		for node in current_level:
			if i == 1:
				current_result.append(node.item)
			else:
				current_result.insert(0,node.item)
			if node.left:
				next_level.append(node.left)
			if node.right:
				next_level.append(node.right)
		i *= -1
		current_level = next_level
		result.append(current_result)
