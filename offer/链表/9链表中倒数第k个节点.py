'''
输入一个链表，输出该链表中倒数第k个结点
'''
def kkk(Head,k):
	fast = Head
	for i in range(k-1):
		fast = fast.next
	slow = Head
	while fast.next:
		fast = fast.next
		slow = slow.next
	return slow