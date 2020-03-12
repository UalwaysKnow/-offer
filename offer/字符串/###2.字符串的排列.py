'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
#理解 见笔记

def permutation(s):
	s_list = list(s)
	n = len(s)
	result = []

	if n<1 or n>9:
		return
	if n == 1:
		return s

	for i in range(len(s)):
		if i > 0 and s[i] == s[i-1]:
			continue
		temp = permutation(''.join(s_list[:i]) + ''.join(s_list[i+1:]))
		for j in temp:
			result.append(s_list[i] + j)

	return result

s = 'abc'
permutation(s)