'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，
第一个只出现一次的字符是"l"。
'''
# l列表存储只出现过一次的字符，s集合存储出现多次的集合
class Solution:
	def __init__(self):
		self.l = []
		self.s = set()
	def FirstAppearingOnce(self):
		if not self.l:
			return #
		else:
			return self.l[0]
	def Insert(self,char):
		if char in self.s:
			pass
		elif char in self.l:
			self.s.add(char)
			self.l.remove(char)
		else:
			self.l.append(char)

#对于列表 append和remove相对应，pop参数为索引，默认为最后一个
#对于集合 discard,remove,pop,clear

s = Solution()
s.Insert('a')
print(s.FirstAppearingOnce())