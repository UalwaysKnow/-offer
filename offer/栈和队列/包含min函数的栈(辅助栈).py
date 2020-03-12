class stack:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def pop(self):
		if len(self.stack1) == 0:
			return None
		if self.stack1[-1] == self.stack2[-1]:
			self.stack2.pop()
		self.stack1.pop()

	def push(self,data):
		self.stack1.append(data)
		if len(self.stack2) == 0 or data < self.stack2[-1]:
			self.stack2.append(data)
	def min(self):
		return self.stack2[-1]

s = stack()
s.push(3)
s.push(2)
s.push(4)
print(s.min())