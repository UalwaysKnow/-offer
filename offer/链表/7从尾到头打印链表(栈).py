'''
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList
'''
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class Linked_list:
	def __init__(self,data_list):
		self.data_list = data_list
		self.head = None
	def initList(self):
		self.head = Node(self.data_list[0])
		temp = self.head
		for i in self.data_list[1:]:
			node = Node(i)
			temp.next = node
			temp = temp.next

	def reverse_print(self):
		stack = []
		temp = self.head
		while temp != None:
			stack.append(temp.data)
			temp = temp.next
		stack = stack[::-1]
		return stack

array = [1,2,3,4,5]
ll = Linked_list(array)
ll.initList()
print(ll.reverse_print())