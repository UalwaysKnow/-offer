'''
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。
'''
# 注意是给定一个节点，而不是给定一个索引
def exchange(node):
	temp = node.next
	node.data, temp.data = temp.data, node.data
	node.next = temp.next