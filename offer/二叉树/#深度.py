def iteration(root):
	if root == None:
		return 0
	if root.left is None and root.right is None:
		return 1
	left_l = iteration(root.left)
	right_l = iteration(root.right)
	return max[left_l,right_l] + 1