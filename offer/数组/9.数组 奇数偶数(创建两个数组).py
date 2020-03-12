'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变
'''
def func(s):
	if len(s) <= 1:
		return -1
	odd_number = []
	even_number = []
	for i in s:
		if i%2 == 1:
			odd_number.append(i)
		else:
			even_number.append(i)
	return odd_number + even_number


s = [1,4,5,3,2,7]
print(func(s))