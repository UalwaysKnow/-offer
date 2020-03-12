'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数
'''
def find(array,target):
	m = len(array)
	n = len(array[0])
	find = False

	if m<=1 or n<=1:
		return -1

	i = 0
	j = n-1

	while i < m and j >= 0:
		if array[i][j] == target:
			find = True
		elif array[i][j] < target:
			i+=1
		else:
			j-=1
	return find