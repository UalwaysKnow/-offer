'''
求1+2+3+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
'''
def count(n):
	if n == 1:
		return 1
	return (n + count(n-1))
print(count(10))