class stack:
	def __init__(self):
		self.stack = []
		self.max = []
	def push(self,num):
		self.stack.append(num)
		if len(self.max) == 0:
			self.max.append(num)
		elif self.max[-1] < num:
			self.max.append(num)
	def pop(self):
		if len(self.stack) == 0:
			return None
		if self.stack[-1] == self.max[-1]:
			self.max.pop()
		temp = self.stack.pop()
		return temp
	def max_num(self):
		return self.max[-1]
	def get_length(self):
		return len(self.stack)

class queue:
	def __init__(self):
		self.stack1 = stack()
		self.stack2 = stack()
	def add(self,num):
		self.stack1.push(num)
	def remove(self):
		if self.stack1.get_length() == 0 and self.stack2.get_length() == 0:
			return None
		if self.stack2.get_length() == 0:
			while self.stack1.get_length() > 0:
				temp = self.stack1.pop()
				self.stack2.push(temp)
			self.stack2.pop()
		else:
			self.stack2.pop()
	def max_num(self):
		# 记住特殊情况
		if self.stack2.get_length() == 0:
			return self.stack1.max_num()
		elif self.stack1.get_length() == 0:
			return self.stack2.max_num()

		if self.stack1.max_num() > self.stack2.max_num():
			return self.stack1.max_num()
		else:
			return self.stack2.max_num()

q = queue()
q.add(1)
q.add(5)
q.add(3)
q.add(4)
q.add(1)
q.add(2)
q.remove()
print(q.max_num())
q.remove()
print(q.max_num())
q.remove()
print(q.max_num())
q.remove()
print(q.max_num())
q.remove()
print(q.max_num())