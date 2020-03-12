'''
求出1~13的整数中1出现的次数,并算出1001300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''
#方法一，遍历
def count_num(num):
	count = 0
	while num>0:
		if num%10 == 1:
			count+=1
		num = num//10
	return count

def sum(n):
	count_1  = 0
	for i in range(1,n+1): # 这里的循环范围不能错了
		count_1 += count_num(i)
	return count_1


#变体：二进制数字n中的1的个数
# 把一个整数减去1，再和原来的整数做相与运算，会把该整数二进制的最右边的1变成0
def count_num_er(n):
	count = 0
	while n>0:
		count+=1
		n = n & (n-1)
	return count

# 方法二，高级一点 理解见笔记
def count_num2(number):
	count = 0
	base = 1
	round = number

	while round > 0:
		weight = round % 10
		round = round // 10
		if weight == 0:
			count += round * base
		elif weight == 1:
			count += round * base + 1 + number % base
		else:
			count += round * base + base
		base *= 10
	return count
print(count_num2(11))