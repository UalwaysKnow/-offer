def insertion_sort(s):
	for i in range(1,len(s)):
		key = s[i]
		j = i-1
		while j >= 0 and key < s[j]:
			s[j+1] = s[j]
			j-=1
		s[j+1] = key
	return s

def kkkk(s,k):
	s_sorted = insertion_sort(s)
	return s_sorted[:k]