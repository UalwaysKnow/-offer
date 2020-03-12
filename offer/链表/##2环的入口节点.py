'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null
'''
def ring(head):
	flag = 0
	fast = head
	slow = head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			flag = 1
			break
	if flag == 0:
		return None

	fast = head
	while fast != slow:
		fast = fast.next
		slow = slow.next
	return fast