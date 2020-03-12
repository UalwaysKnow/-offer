'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''
def quik_sort(s,start,end):
	if start >= end:
		return
	mid = s[start]
	low = start
	high = end

	while low < high:
		while low < high and s[high] >= mid:
			high -= 1
		s[low] = s[high]
		while low < high and s[low] < mid:
			low += 1
		s[high] = s[low]

		s[low] = mid

		quik_sort(s, start, low-1)
		quik_sort(s, low+1, end)

def nixudui(s):
	original_array = s.copy()
	quik_sort(s, 0, len(s) - 1)
	count = 0
	for i in s:
		pos = original_array.index(i)
		count += pos
		original_array.pop(pos)
	return count

s = [9,3,4,5,3]
print(nixudui(s))
