'''
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，
即“XYZdefabc”。是不是很简单？OK，搞定它！
'''
def method1(s,num):
	return s[num:len(s)] + s[0:num]

def reverse(s):
	start = 0
	end = len(s)-1
	while start < end:
		s[start], s[end] = s[end], s[start]
		start+=1
		end-=1
	return s

# TypeError: 'str' object does not support item assignment

def method2(s,num):
	s = list(s)
	s = reverse(s)
	s1 = s[0:len(s) - num]
	s2 = s[len(s) - num:len(s)]
	s1 = reverse(s1)
	s2 = reverse(s2)
	return ''.join(s1) + ''.join(s2)



print(method1('abcXYZdef',3))