'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
# 利用哈希表实现，空间转时间方法，时间复杂度由o(n^2)降为o(n),空间复杂度增加为o(n)
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.random = None
# class solution:
# 	def __init__(self,data_list):
# 		self.data_list = data_list
# 		self.head = None
# 	def initList(self):
# 		self.head = Node(self.data_list[0])
# 		temp = self.head
# 		temp.random = self.head
# 		for i in self.data_list[1:]:
# 			node = Node(i)
# 			temp.next = node
# 			temp = temp.next
# 			temp.random = self.head
# 		return self.head

	def copy(self,old_head):
		# 先创建两个指针
		old = old_head
		new_head = Node(old_head.data)
		new = new_head
		Hash = {}
		Hash[new.data] = new
		# 先复制一遍链表（除了random指针）
		while old and old.next:
			old = old.next
			temp = Node(old.data)
			new.next = temp
			new = new.next
			Hash[new.data] = Node(new.data)
		# 再从头开始遍历，根据哈希表将random指针填上;考虑random指针指向None的情况
		new = new_head
		old = old_head
		while new:
			if old.random != None:
				new.random = Hash[old.random.data]
			new = new.next
			old = old.next
		return new_head

# test
# s = [1,2,3,4]
# ll = solution(s)
# old_head = ll.initList()
# print(old_head)
# print(ll.copy(old_head))