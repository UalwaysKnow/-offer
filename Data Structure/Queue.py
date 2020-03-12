class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

class Queue():
	def __init__(self):
		self.head = None

	def entry(self,item):
		temp = Node(item)
		if self.head == None:
			self.head = temp
		else:
			temp.next = self.head
			self.head = temp

	def out(self):
		if self.head == None:
			print("error")
		else:
			temp = self.head
			while temp.next != None:
				prev = temp
				temp = temp.next
			prev.next = None
			temp = None

	def print(self):
		temp = self.head
		list = []
		while temp != None:
			list.append(temp.data)
			temp = temp.next
		print(list)

Q = Queue()
Q.entry(1)
Q.entry(2)
Q.entry(3)
Q.out()
Q.print()