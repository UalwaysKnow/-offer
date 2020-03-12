'''
返回数列中的第n个值
核心：拆解为子问题
下面两题相同，区别在于初始项为第一项（而非第0项），初始值fn1，fn2 = 2,1
跳台阶问题：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
矩形覆盖问题
们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个21的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
def method(n):
	if n < 0 or n > 39:
		return False
	fn1=1
	fn2=0
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		for i in range(2,n+1):
			fn = fn1+fn2
			fn2 = fn1
			fn1 = fn
		return fn
