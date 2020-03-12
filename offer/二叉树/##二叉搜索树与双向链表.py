'''输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链
表。要求不能创建任何新的结点，只能调整树中结点指针的指向。'''
### 明确二叉搜索树和堆的区别
# 应用中序遍历的方法
class solution:
	def __init__(self):
		self.tree = []
	def iteration(self,root):
		if root is None:
			return
		self.iteration(root.left)
		self.tree.append(root)
		self.iteration(root.right)
	def change(self):
		self.tree[0].left = None
		self.tree[-1].right = None
		for i in range(1,len(self.tree)-1):
			self.tree[i].left = self.tree[i-1]
			self.tree[i].right = self.tree[i+1]
		return self.tree


# 正规方法：
class solution:
	def __init__(self):
		self.listhead = None
		self.listtail = None
	def convert(self,root):
		if root is None:
			return
		self.convert(root.left)
		if self.listhead == None:
			self.listhead = root
			self.listtail = root
		else:
			self.listtail.right = root
			root.left = self.listtail
			self.listtail = root
		self.convert(root.right)
		return self.listhead