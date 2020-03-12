'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
def xuanzhuan(s):
	for i in range(len(s)-1):
		if s[i] < s[i+1]:
			return s[i]

#修改题目，来求旋转数组的某个值
# s[mid] < s[right] 说明右半段有序；s[mid] > s[left]说明左半段有序
def erfen(s,key):
	find = False
	left = 0
	right = len(s)-1
	while left<right:
		mid = (left + right) // 2
		if s[mid] == key:
			find = True
			return find
		elif s[mid] < s[right]:
			if s[mid] <= key and key <= s[right]:
				left = mid +1
			else:
				right = mid -1
		elif s[mid] > s[left]:
			if s[left] < key and key < s[mid]:
				right = mid -1
			else:
				left = mid + 1
	return find