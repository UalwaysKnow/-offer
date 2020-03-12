'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
from functools import cmp_to_key

def comp(x,y):
	if (str(x)+str(y)) < (str(y)+str(x)):
		return -1
	else:
		return 1

def MinNumber(array):
	if array is None or len(array) == 0:
		return

	array = [str(i) for i in array]
	array.sort(key=cmp_to_key(comp))

	return "".join(array)

s = [32,43,21]
print(MinNumber(s))