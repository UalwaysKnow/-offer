'''给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8） 中，按结点数值大小顺序第三小结点的值为4。'''
class solution:
	def __init__(self):
		self.array = []

	def method(self,root):
		if root == None:
			return
		self.method(root)
		self.array.append(root)
		self.method(root)

	def result(self,k):
		return self.array[k]