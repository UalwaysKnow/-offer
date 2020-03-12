'''
利用两个栈实现队列
'''
class queue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def push(self,data):
		self.stack1.append(data)
	def pop(self):
		if len(self.stack1) == 0:
			return None
		if len(self.stack2) != 0:
			result = self.stack2.pop()
		else:
			while len(self.stack1) > 0:
				temp = self.stack1.pop()
				self.stack2.append(temp)
			result = self.stack2.pop()
		return result

q = queue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())