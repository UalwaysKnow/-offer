'''
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返
回值的list中，数组长度大的数组靠前)
'''
class Node:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None

def initTree():
	root = Node(10)
	node = root
	node.left = Node(5)
	node.right = Node(12)
	node = root.left
	node.left = Node(4)
	node.right = Node(7)
	return root

def maopao_sort(result,result_length):
	for i in range(len(result_length)-1):
		for j in range(len(result_length)-i-1):
			if result_length[j] < result_length[j+1]:
				result_length[j],result_length[j+1] = result_length[j+1],result_length[j]
				result[j],result[j+1] = result[j+1],result[j]
	return result

def method(root,expectnumber):
	if root is None:
		return
	result = [] # 所有路径的合集
	result_length = []
	path = []
	def iteration(root,expectnumber):
		if root.item < expectnumber:
			path.append(root.item)
			if root.left:
				iteration(root.left,expectnumber - root.item)
			if root.right:
				iteration(root.right,expectnumber - root.item)
		elif root.item == expectnumber:
			path.append(root.item)
			if root.left is None and root.right is None:
				temp = path[:]
				result.append(temp)
				result_length.append(len(temp))
		else:
			path.append(0) # append 0 仅仅是为了与前两个选项同步！
		path.pop()
	iteration(root,expectnumber)
	return maopao_sort(result,result_length)

if __name__ == "__main__":
	root = initTree()
	print(method(root,22))