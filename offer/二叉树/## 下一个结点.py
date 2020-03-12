'''给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结
点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。'''
# 两种情况： 1.下一个结点是其右孩子，2.是第一个使其在该节点的左子树的节点
def nextnode(target):
	if target == None:
		return None
	elif target.right:
		temp = target.right
		while temp.left:
			temp = temp.left
		return temp
	else:
		while target.father:
			temp = target.father
			if target == temp.left:
				return temp
			target = temp