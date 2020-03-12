class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#头指针呢？？？？
class Linked_List:
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

	def is_empty(self):
		return self.head == None

	def get_length(self):
		temp = self.head
		length = 0
		while temp != None:
			length = length + 1
			temp = temp.next
		return length

	def search(self,item):
		temp = self.head
		while temp != None:
			if item == temp.data:
				return True
			temp = temp.next
		return False

	def insert(self,key,item):
		if key<0 or key>self.get_length()-1:
			return False
		temp = self.head
		i = 0
		while i<key:
			temp = temp.next
			i = i+1
		node = Node(item)
		node.next = temp
		temp.next = node

	def remove(self,key):
		if key<0 or key>self.get_length()-1:
			return False
		temp = self.head
		i = 0
		while i<key:
			pre = temp
			temp = temp.next
			i = i+1
			if i == key:
				pre.next = temp.next
		pre = None

	def print(self):
		print("Linked_List:")
		list = []
		temp = self.head
		while temp != None:
			list.append(temp.data)
			temp = temp.next
		print(list)
	# 比较困难，难理解
	def reverse(self):
		prev = None
		current = self.head
		while current:
			next_node = current.next
			current.next = prev
			next_node.next = current
			prev = current



data_list = [1,2,3,4,5,6,7,8]
ll = Linked_List(data_list)
ll.initList()
ll.remove(2)
ll.print()