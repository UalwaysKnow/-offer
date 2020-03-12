# o(n)的做法就是挨个数
# o(logn)的做法使用二分法查找

def erfen(s,target):
	if s is None or len(s) == 0:
		return -1
	left = 0
	right = len(s)-1

	if s[left] > s[right]:
		s = s[::-1]

	while left <= right:
		mid = (left + right) //2
		if s[mid] > target:
			right = mid - 1
		elif s[mid] < target:
			left = mid + 1
		else:
			target_index = mid
			break

	count = 1
	i = target_index + 1
	while i<len(s) and s[i] == s[target_index]:
		i+=1
		count+=1
	i = target_index - 1
	while i>=0 and s[i] == s[target_index]:
		i-=1
		count+=1
	return count

s = [1,2,3,3,3,4,5,6,7,8,9,9,9]
print(erfen(s,9))