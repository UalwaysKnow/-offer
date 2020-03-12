#冒泡排序是从后往前排序好的
def bubblesort(s):
	for i in range(len(s)-1):
		for j in range(len(s)-i-1):
			if s[j+1]<s[j]:
				s[j+1],s[j] = s[j], s[j+1]
	return s

s = [6,5,3,4,5,6,7]
print(bubblesort(s))