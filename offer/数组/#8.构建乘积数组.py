'''
给定一个数组A[0,1,...,n−1]A[0,1,...,n−1]      A[0,1,...,n-1]A[0,1,...,n−1],
请构建一个数组B[0,1,...,n−1]B[0,1,...,n−1]      B[0,1,...,n-1]B[0,1,...,n−1],
其中B中的元素B[i]=A[0]∗A[1]∗...∗A[i−1]∗A[i+1]∗...∗A[n−1]B[i]=A[0]∗A[1]∗...∗A[i−1]∗A[i+1]∗...∗A[n−1]
 B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]B[i]=A[0]∗A[1]∗...∗A[i−1]∗A[i+1]∗...∗A[n−1]。不能使用除法。
'''

# 未知bug，总之不能用 B_array = [A for i in range(3)] 语句创建

def multiply(A):
	B_array = [[1 if i==j else A[j] for j in range(len(A))] for i in range(len(A))]

	B = []
	for i in range(len(A)):
		temp = 1
		for j in B_array[i]:
			temp *= j
		B.append(temp)
	return B

A = [1,2,3]
print(multiply(A))