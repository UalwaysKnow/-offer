'''
两个题思路其实是一样的：
1.一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0到n-1之内。
在范围0到n-1的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
2.假设一个单调递增的数组里的每个元素都是整数并且是唯一的。
请编程实现一个函数找出数组中任意一个数值等于其下标的元素。
例如，在数组[-3, -1, 1, 3, 5]中，数字3和它的下标相等。
'''
def find(list):
	left = 0
	right = len(list)-1
	mid = (left+right)//2
	while left<=right:
		if mid == list[mid] and (mid+2) == list[mid+1]:
			return mid+1
		elif mid == list[mid]:
			left = mid+1
		else:
			right = mid-1
		mid = (left+right)//2

s = [0,1,2,3,4,5,7,8,9]
print(find(s))