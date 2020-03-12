'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字.
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0
'''
def quick_sort(s,start,end):
	if start >= end:
		return
	low = start
	high = end
	mid = s[start]

	while low < high:
		while low < high and s[high] >= mid:
			high-=1
		s[low] = s[high]
		while low < high and s[low] < mid:
			low+=1
		s[high] = s[low]

		s[low] = mid

		quick_sort(s,low+1,end)
		quick_sort(s,start,low-1)

def count(array):
	quick_sort(array,0,len(array)-1)
	mid_index = (len(array)-1)//2
	mid = array[mid_index]

	count = 0
	for i in array:
		if i == mid:
			count+=1

	if count > len(array)//2:
		return mid
	else:
		return None

s = [1,2,3,4,5,2,2,2,2]
print(count(s))