'''
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
def finds(array,s):
	i = 0
	j = len(array)-1
	A = []
	B = []
	while i<=j:
		if array[i] + array[j] == s:
			A.append(array[i])
			B.append(array[j])
		elif array[i] + array[j] < s:
			i += 1
		else:
			j -= 1
	if len(A) == 1:
		return A.pop(),B.pop()
	elif len(A) == 0:
		return None
	else:
		C = []
		for i in range(len(A)):
			C.append(A[i]*B[i])
		return A[C.index(min(C))],B[C.index(min(C))]

