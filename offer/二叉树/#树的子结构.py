'''输入两棵二叉树A，B，判断B是不是A的子结构'''
def Issubtree(rootA,rootB):
	if rootA == None:
		return False
	if rootB == None:
		return True
	if rootA.value == rootB.value:
		return Issubtree(rootA.left,rootB.right) and Issubtree(rootA.right,rootB.right)

def Hassubtree(root1,root2):
	if root1 is None or root2 is None:
		return False
	flag = 1
	if root1.value == root2.value:
		flag = Issubtree(root1,root2)
	if flag == 1:
		return True
	else:
		return Hassubtree(root1.left,root2) or Hassubtree(root1.right,root2)
