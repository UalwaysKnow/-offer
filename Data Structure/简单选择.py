def selectsort(s):
	for i in range(len(s)-1):
		for j in range(i,len(s)):
			if s[i] > s[j]:
				s[i], s[j] = s[j], s[i]
	return s

s = [4,3,2,9,5,7,5,4,3]
print(selectsort(s))