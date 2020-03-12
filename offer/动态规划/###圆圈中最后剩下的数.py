'''
0, 1, …, n-1这n个数字(n>0)排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字。
'''
def method(n,m):
	if n == 0:
		return None
	elif n == 1:
		return 0
	fn_1 = 0
	for i in range(2,n+1):
		fn = (fn_1 + m) % n
		fn_1 = fn
	return fn