'''
输入两个链表，找出它们的第一个公共结点。
'''
# 方法一，获得两个的长度，计算差，然后同时遍历到公共节点
def method1(head1,head2):
	curr1 = head1
	curr2 = head2
	count1 = 0
	count2 = 0
	while curr1:
		count1 +=1
		curr1 = curr1.next
	while curr2:
		count2 += 1
		curr2 = curr2.next
	div = abs(count1-count2)
	flag = 1
	if count1 < count2:
		flag = 0

	curr1 = head1
	curr2 = head2
	if flag:
		for i in range(div):
			curr1 = curr1.next
	else:
		for i in range(div):
			curr2 = curr2.next

	while curr1 != curr2:
		curr1 = curr1.next
		curr2 = curr2.next
	return curr1

# 方法二，利用两个辅助栈先分别存放两个链表的节点
def method2(head1,head2):
	stack1 = []
	stack2 = []
	while head1:
		stack1.append(head1)
		head1 = head1.next
	while head2:
		stack2.append(head2)
		head2 = head2.next
	while stack1 != None and stack2 != None:
		for i in range(len(stack1)):
			if stack1[-1] == stack2[-1]:
				temp = stack1[-1]
				stack1.pop()
				stack2.pop()
			else:
				return temp
	return None