def quicksort(s,start,end):
	#递归退出的条件
	if start>=end:
		return
	mid = s[start]
	low = start
	high = end

	while low < high:
		while low < high and s[high]>=mid:
			high-=1

		s[low] = s[high]

		while low < high and s[low]<mid:
			low+=1
		s[high] = s[low]

	s[low] = mid

	quicksort(s,start,low-1)
	quicksort(s,low+1,end)

s = [3,2,3,5,6,7,7,8,6,5,4,3,2,4,5,6,6]
quicksort(s,0,len(s)-1)
print(s)
