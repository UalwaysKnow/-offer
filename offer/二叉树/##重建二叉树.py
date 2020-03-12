'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如
输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,
3,8,6}，则重建二叉树并返回。
'''
class TreeNode:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None

def reconstruction(pre,mid):
	if set(pre) == set(mid):
		return None
	if len(pre) == 0:
		return None
	root_rebuild = TreeNode(pre[0])
	i = mid.index(pre[0])
	root_rebuild.left = reconstruction(pre[1:i+1], mid[:i])
	root_rebuild.right = reconstruction(pre[i+1:], mid[i+1:])
	return root_rebuild