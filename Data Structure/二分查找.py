#前提必须是有序数组
def feidigui(s,num):
	left = 0
	right = len(s)-1
	while left <= right:
		mid = (left+right)//2
		if num < s[mid]:
			right = mid - 1
		elif num > s[mid]:
			left = mid + 1
		else:
			return mid
	return None

def digui(s,num,left,right):
	if left >= right:
		return None
	mid = (left+right)//2
	if num > s[mid]:
		left = mid + 1
		return digui(s,num,left,right)
	elif num <s[mid]:
		right = mid - 1
		return digui(s,num,left,right)
	else:
		return mid

s = [1,2,3,4,5,6,7,8]
s.sort()
print(digui(s,6,0,len(s)-1))