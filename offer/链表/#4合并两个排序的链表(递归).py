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
		return self.head

def method1(A_head,B_head):
	if A_head == None or B_head == None:
		return None

	if A_head.data < B_head.data:
		head = A_head
		insertL = B_head
	else:
		head = B_head
		insertL = A_head

	curr = head
	while insertL:
		if curr.next == None:
			curr.next = insertL
			curr = curr.next
			insertL = insertL.next
		elif insertL.data >= curr.data and insertL.data < curr.next.data:
			temp = Node(insertL.data)
			temp.next = curr.next
			curr.next = temp
			curr = curr.next
			insertL = insertL.next
		else:
			curr = curr.next
	return head

# 看不懂
def method2(A_head,B_head):
	if A_head == None:
		return B_head
	elif B_head == None:
		return A_head
	if A_head.data < B_head.data:
		A_head.next = method2(A_head.next,B_head)
		return A_head
	else:
		B_head.next = method2(A_head,B_head.next)
		return B_head

def print_list(result1,result2):
	result = method1(result1, result2)
	while result:
		print(result.data)
		result = result.next

s1 = [1,3,5,7,9]
s2 = [2,4,6,8]
l1 = Linked_list(s1)
l2 = Linked_list(s2)
result1 = l1.initList()
result2 = l2.initList()

print_list(result1,result2)