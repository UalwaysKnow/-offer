'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# 动态规划法
'''
因为每个数字只能除以2、3、5，所以查看序列的一种方法是将序列拆分为以下三组：
     (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
即所有的丑数依次乘以2,3,5
'''
def ugly_number(n):
	if n < 1:
		return None
	if n == 1:
		return 1
	t2=0
	t3=0
	t5=0
	Number = []
	Number.append(1)
	for i in range(n):
		Number.append(min(Number[t2]*2,Number[t3]*3,Number[t5]*5))
		if Number[i+1] == Number[t2]*2:
			t2+=1
		if Number[i+1] == Number[t3]*3:
			t3+=1
		if Number[i+1] == Number[t5]*5:
			t5+=1
	return Number[n-1]
print(ugly_number(7))
