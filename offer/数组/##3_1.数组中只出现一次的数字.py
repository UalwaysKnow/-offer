'''
数组中只有一个数字出现1次，其余出现三次，找到这个只出现一次的数字
'''
def find_number(array):
	new_array = [0 for i in range(32)]
	for i in array:
		mod = i
		j = 0
		while mod >= 1:
			new_array[j] += mod % 2
			mod = mod // 2
			j += 1
	for i in range(32):
		new_array[i] = new_array[i]%3
	#return new_array
	final_result = 0
	for i in range(32):
		final_result = final_result + new_array[i] * pow(2,i)
	return final_result

s = [3,3,3,1,1,1,2,2,2,5]
print(find_number(s))
