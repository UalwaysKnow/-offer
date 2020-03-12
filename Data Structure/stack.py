#数组栈和链表栈
class Stack1:
	def __init__(self, limit=10):
		self.stack = []
		self.limit = limit

	def push(self,data):
		if len(self.stack)<=self.limit:
			self.stack.append(data)
		else:
			print("error!")

	def pop(self):
		if len(self.stack) > 0:
			self.stack.pop()
		else:
			print("error")

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack2:
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None

	def push(self,item):
		new_node = Node(item)
		temp = self.head
		if temp == None:
			self.head = new_node
		else:
			self.head = new_node
			self.head.next = temp

	def pop(self):
		if self.is_empty():
			print("error")
		else:
			temp = self.head.next
			self.head = None
			self.head = temp

	def print(self):
		temp = self.head
		list = []
		while temp != None:
			list.append(temp.data)
			temp = temp.next
		print(list)

stack = Stack2()
stack.push(19)
stack.push(5)
stack.pop()
stack.print()