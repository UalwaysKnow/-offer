'''
三种情况：
1.二叉搜索树：根据性质
2.有指向父亲节点的指针：直接比较元素
3.两个条件都没有
'''
def method(root,p,q):
	if root is None:
		return None
	if root == p or root == q:
		return root
	left = method(root.left,p,q)
	right = method(root.right,p,q)
	if left != None and right != None:
		return root
	if left is None:
		return right
	elif right is None:
		return left