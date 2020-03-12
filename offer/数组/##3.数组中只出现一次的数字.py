'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
def getfirst1(num):
	n=0
	while num & (1<<n) == 0:
		n+=1
	return 1<<n

def find_number(array):
	temp = array[0]
	for i in range(1,len(array)):
		temp = temp^array[i]
	if temp == 0:
		return None
	else:
		first1 = getfirst1(temp)

	a = []
	b = []

	for i in range(len(array)):
		if array[i] & first1 == 0:
			a.append(array[i])
		else:
			b.append(array[i])

	result_a = a[0]
	for i in range(1,len(a)):
		result_a ^= a[i]
	result_b = b[0]
	for i in range(1, len(b)):
		result_b ^= b[i]

	return result_a,result_b

s = [1,4,4,1,5,6,3,2,3,6]
print(find_number(s))