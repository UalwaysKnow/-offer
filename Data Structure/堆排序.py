def siftdown(elems,e,begin,end): # 向下筛选
	i,j = begin, begin*2+1 # j为i的左孩子
	while j < end:
		if j+1 < end and elems[j] > elems[j+1]: #若左子节点大于右子节点，则将j指向右子节点
			j+=1
		if e < elems[j]: #j已经指向两个子节点中较小的位置
			break        #如果插入元素e小于j位置的值，则为三者中最小的
		elems[i] = elems[j] #能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父节点的位置
		i,j = j, j*2+1 #更新i为被上移为父节点的原来的j的位置，更新j为更新后i位置的左子节点
	elems[i] = e    #如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父节点
					#或者位置i已经更新到叶节点位置，则将e赋给这个叶节点
def heap_sort(elems):
	end = len(elems) #构造堆序
	for i in range(end//2-1,-1,-1):
		siftdown(elems,elems[i],i,end)
	for i in range((end-1),0,-1): #进行堆排序，i最后一个值为1，不需要到0
		print(elems)
		e = elems[i] # 将末尾元素赋给e
		elems[i] = elems[0] # 交换对顶与最后一个元素
		siftdown(elems,e,0,i)
	return (elems)

if __name__ == "__main__":
	print(heap_sort([5,6,8,1,2,4,9]))