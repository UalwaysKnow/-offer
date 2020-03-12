class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

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
			node.prev = temp
			temp = temp.next

	def print(self):
		temp = self.head
		list = []
		while temp != None:
			list.append(temp.data)
			temp = temp.next
		print(list)

	def get_length(self):
		temp = self.head
		length = 0
		while temp != None:
			length = length+1
			temp = temp.next
		return length

	def insert(self,key,value):
		if key < 0 or key > self.get_length():
			return False
		i = 0
		temp = self.head
		node = Node(value)
		while i < key-1:
			temp = temp.next
			i = i+1
		next_node = temp.next
		temp.next = node
		node.prev = temp
		node.next = next_node
		next_node.prev = node

	def remove(self,key):
		if key<0 or key>self.get_length():
			return False
		temp = self.head
		i=0

		while i < key:
			temp = temp.next
			i = i+1
		next_node = temp.next
		next_node.prev = temp.prev

		prev_node = temp.prev
		prev_node.next = temp.next

		temp = None


data_list = [1,2,3,4,5,6]
ll = Linked_List(data_list)
ll.initList()
ll.insert(2,9)
ll.remove(2)
ll.print()