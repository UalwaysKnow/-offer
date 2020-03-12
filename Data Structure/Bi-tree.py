class Node:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.item) #print一个node类时会打印__str__的返回值

class Tree:
	def __init__(self):
		self.root = Node('root') # 作为哨兵使用
	def add(self,item):
		node = Node(item)
		if self.root is None:
			self.root = node
		q = [self.root]
		while q:
			pop_node = q.pop(0)
			if pop_node.left is None:
				pop_node.left = node
				return
			elif pop_node.right is None:
				pop_node.right = node
				return
			else:
				q.append(pop_node.left)
				q.append(pop_node.right)
	def get_parent(self,item):
		if self.root.item == item:
			return None
		temp = [self.root]
		while temp:
			pop_node = temp.pop(0)
			if pop_node.left and pop_node.left.item == item:
				return pop_node
			if pop_node.right and pop_node.left.item == item:
				return pop_node
			if pop_node.left is not None:
				temp.append(pop_node.left)
			if pop_node.right is not None:
				temp.append(pop_node.right)
	def delete(self,item):
		if self.root is None:
			return None
		parent = self.get_parent(item)
		if parent:
			del_node = parent.left if parent.left.item == item else parent.right
			# 四种情况，第四种是指叶子节点，第四种情况有两步替换
			if del_node.left is None:
				if parent.left.item == item:
					parent.left = del_node.right
				else:
					parent.right = del_node.right
			elif del_node.right is None:
				if parent.left.item == item:
					parent.left = del_node.right
				else:
					parent.right = del_node.right
			else:
				temp_pre = del_node
				temp_next = del_node.right
				if temp_next.left is None:
					temp_pre.right = temp_next.right ###找到值合适的节点，并替换删除节点的右孩子
					temp_next.left = del_node.left
					temp_next.right = del_node.right
				else:
					while temp_next.left:
						temp_pre = temp_next
						temp_next = temp_next.left
					temp_pre.left = temp_next.right ### 找到值合适的节点，并替换删除节点的左孩子
					temp_next.left = del_node.left
					temp_next.lfet = del_node.right
				# tihuan
				if parent.left.item == item:
					parent.left = temp_next
				else:
					parent.right = temp_next
				del del_node
				return True
		else:
			return False
