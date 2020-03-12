'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
'''
def method(in_list,out_list):
	stack = []
	i = 0
	j = 0
	while i < len(in_list) and j < len(out_list): #问题！！！stack本来就为空，压根没有进入循环！
		stack.append(in_list[i])
		if (i == len(in_list) - 1) and stack[-1] != out_list[j]:
			return False
		if stack[-1] == out_list[j]:
			stack.pop()
			j+=1
		i += 1
	return True

s1 = [1,2,3,4,5]
s2 = [4,5,3,2,1]
print(method(s1,s2))