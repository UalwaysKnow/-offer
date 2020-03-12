class Node:
	def __init__(self,item):
		self.item = item
		self.isin = False
		self.left = None
		self.right = None

class HuffmanTree:
	def __init__(self,l):
		self.li = []
		for x in range(0,len(l)):
			self.li.append(Node(l[x]))
		K = Node(float('inf'))
		while len(self.li) < 2*len(l)-1:
			m1=m2=K
			for x in range(0,len(self.li)):
				if m1.item>self.li[x].item and (self.li[x].isin is False):
					m2 = m1
					m1 = self.li[x]
				elif m2.item>self.li[x].item and (self.li[x].isin is False):
					m2 = self.li[x]

			H=Node(m1.item+m2.item)
			H.right = m1
			H.left  = m2
			self.li.append(H)
			m1.isin = m2.isin = True
			print(m1.item,m2.item,H.item)