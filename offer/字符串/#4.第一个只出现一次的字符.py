'''
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）
'''
def find(s):
	dict = {}
	for i in s:
		if i in dict:
			dict[i] += 1
		else:
			dict[i] = 1
	for i in s:
		if dict[i] == 1:
			return s.index(i)
	return -1

s = 'abcdef'
print(find(s))

# 取出来key和value的操作
# for key in dict.keys():
# for value in dict.values():