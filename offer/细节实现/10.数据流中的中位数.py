class solution:
	def __init__(self):
		self.list = []
	def insert(self,num):
		if self.list is None:
			self.list.append(num)
		if num > self.list[-1]:
			self.list.append(num)
		else:
			for i in range(len(self.list)):
				if num <= self.list[i]: ###############################################
					self.list.insert(i,num)
					break
	def getMid(self):
		length = len(self.list)
		mid = (len(self.list)-1)//2
		if length%2 == 1:
			return self.list[mid]
		else:
			mid_num = (self.list[mid]+self.list[mid+1])/2
			return mid_num