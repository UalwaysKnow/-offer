'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

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

	#因为头节点有可能被删除，因此要在头节点前面加上一个节点
	def deleteduplication(self):
		pHead = self.head
		self.first = Node(-1)
		self.first.next = pHead
		curr = self.first #需要记录最后一个不重复的节点
		while pHead and pHead.next:
			if pHead.data == pHead.next.data:
				while pHead.next and pHead.data == pHead.next.data:
					pHead = pHead.next
				curr.next = pHead.next
			else:
				curr = pHead
				pHead = pHead.next

	def print(self):
		temp = self.first
		while temp:
			print(temp.data)
			temp = temp.next

array = [1,2,2,3,4,4,5]
ll = Linked_List(array)
ll.initList()
ll.deleteduplication()
ll.print()