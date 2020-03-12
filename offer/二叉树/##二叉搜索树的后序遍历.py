'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
def method(array):
	if len(array) == 0:
		return None
	root = array[-1]
	# 找到左右子树的分支
	i = 0
	for node in array[:-1]:
		if node > root:
			break
		i+=1
	for node in array[i:-1]:
		if node < root:
			return False
	left = True
	if i>1: #### 判断条件！！
		left = method(array[:i])
	right = True
	if i<len(array)-1 and left:
		right = method(array[i,-1])
	return (left and right)