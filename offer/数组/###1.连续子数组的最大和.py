'''
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''
# 还是用动态规划法的思想比较靠谱
'''
思路分析

1、状态方程 ： max( dp[ i ] )  = getMax(  max( dp[ i -1 ] ) + arr[ i ] ,arr[ i ] ) 

2、上面式子的意义是：我们从头开始遍历数组，遍历到数组元素 arr[ i ] 时，连续的最大的和 可能为 max( dp[ i -1 ] ) + arr[ i ] ，也可能为 arr[ i ] ，做比较即可得出哪个更大，取最大值。时间复杂度为 n。
'''
def MAX(array):
	if array == None or len(array) == 0:
		return
	if len(array) == 1:
		return(array[0])

	final_max = array[0]
	sum = 0

	for i in range(len(array)):
		sum += array[i]
		#下面这个比较最关键
		if sum < array[i]:
			sum = array[i]

		if final_max < sum:
			final_max = sum