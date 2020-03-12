#插入排序是从前往后排序好的
def insertionsort(s):
	count_swap = 0
	for i in range(1,len(s)):
		key = s[i]
		j = i-1 #待比较的前一个元素
		while j>=0 and key < s[j]:
			s[j+1] = s[j]
			j-=1 #这个操作是为了跳出循环，否则j指向第一个数时永远无法跳出循环：j=0
			count_swap += 1
		s[j+1] = key
	return s
s = [2,1,4,2,1]
a = insertionsort(s)
print(a)