'''给定一个整数数组和一个目标值，找出数组中和为目标值的 两个 数。'''
def method(array,s):
	Hash = {}
	for i in array:
		Hash[i] = array.index(i)
	for i in array:
		if (s-i) in Hash:
			return [Hash[i],Hash[s-i]]