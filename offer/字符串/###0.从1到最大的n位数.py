'''
输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则打印出1、2、3一直到最大的3位数即999。
'''
# 该题若考虑大数情况，得用字符串模拟

def method1(n):
	number = 1
	for i in range(n):
		number*=10
	for i in range(number):
		print(i)

#def method2(n):
	