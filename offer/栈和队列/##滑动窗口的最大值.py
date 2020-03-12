'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一
共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组
{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}，
 {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,
 2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''
# 注意问题：当queue为空时，任何索引都会有bug

def method(array,size):
	if array is None or len(array) < 1 or size == 0:
		return []

	queue = []
	max = []
	for i in range(len(array)):
		print(queue)
		if queue:
			if (i-array.index(queue[0])) >= size:
				queue.pop(0)
		if queue == [] or queue[-1]>=array[i]:
			queue.append(array[i])
		else:
			while queue[-1]<array[i]:
				queue.pop()
				if len(queue) == 0:
					break
			queue.append(array[i])
		if i >= (size-1):
			max.append(queue[0])
	return max
s = [2,3,4,2,6,2,5,1]
print(method(s,3))
