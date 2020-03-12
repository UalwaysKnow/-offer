'''
将一个骰子投掷n次，获得的总点数为s，s的可能范围为n~6n。
掷出某一点数，可能有多种掷法，例如投掷2次，掷出3点，共有[1,2],[2,1]两种掷法。
请求出投掷n次，掷出n~6n点分别有多少种掷法。
f（n,k）表示掷n次骰子，最终得和为k的次数。
f（n,k）= f（n-1,k-1）+ f（n-1,k-2）+ f（n-1,k-3）+ f（n-1,k-4）+ f（n-1,k-5）+ f（n-1,k-6）
f(1,1)= f(1,2)= f(1,3)= f(1,4)= f(1,5)= f(1,6)= 1
'''

# 动态规划法
def method(n):
	if n < 1 or n is None:
		return None
	f1 = [1]*6
	if n == 1:
		return f1

	#动态规划
	fn_1 = f1 # n-1时有效和值的次数统计
	for i in range(2,n+1):
		fn = [0]*(6*i-i+1) # 和值k_sum有效范围[n,6*n]，存储到相应数组的相应位置
		for k in range(len(fn)):
			k_sum = k + i # 有效和值应为n+k,k的范围是[0,5*n]
			for j in range(1,7): # 执行计算公式 f(n,k) = ...
				if 6*(i-1) >= k_sum - j >= i-1: # 判断条件：投掷该次之前的和值是否满足范围
					fn[k] += fn_1[k_sum - j - (i-1)] # 求对应的fn_1中对应的k值，即索引
		fn_1 = fn
	return fn

