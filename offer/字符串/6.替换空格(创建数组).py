'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
def tihuan(s):
	final = []
	for i in s:
		if i != ' ':
			final.append(i)
		else:
			final.append('%20')
	return ''.join(final)

s = 'We are family.'
print(tihuan(s))