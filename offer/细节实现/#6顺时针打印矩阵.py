# 设置矩阵的打印边界
def print_matrix(matrix):
	if len(matrix) < 1 or len(matrix[0]) < 1:
		return None
	elif len(matrix) == 1 or len(matrix[0]) == 1:
		return matrix
	array = []
	a = 0
	b = len(matrix[0])
	c = len(matrix)
	d = 0

	while a <= b and d <= c:
		for i in range(d,b-1):
			array.append(matrix[a][i])
		for i in range(a,c-1):
			array.append(matrix[i][b-1])
		for i in range(b-1,d,-1):
			array.append(matrix[c-1][i])
		for i in range(c-1,a,-1):
			array.append(matrix[i][d])
		a+=1
		b-=1
		c-=1
		d+=1
	print(array)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print_matrix(matrix)