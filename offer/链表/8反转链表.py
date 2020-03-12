'''
输入一个链表，反转链表后，输出新链表的表头。
'''
def reverse(head):
	current = head
	prev = None
	while current.next:
		next_node = current.next
		current.next = prev
		next_node.next = current
		prev = current
	return current.next