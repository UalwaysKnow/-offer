'''
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。
'''
def quick_sort(s,start,end):
	if start >= end:
		return
	mid = s[start]
	low = start
	high = end

	while low < high:
		while low < high and s[high] >= mid:#快速排序一定要注意这个
			high-=1
		s[low] = s[high]
		while low < high and s[low] < mid:
			low+=1
		s[high] = s[low]

		s[low] = mid

		quick_sort(s,low+1,end)
		quick_sort(s,start,low-1)

def duplicate(s):
	#不可忘记边界条件
	if s == None or len(s)<=1:
		return -1
	for i in range(len(s)):
		if i<0 or i >len(s)-1:
			return -1

	quick_sort(s,0,len(s)-1)
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return s[i]
	return -1

s = [2,4,3,5,7,3,2,9]
print(duplicate(s))
