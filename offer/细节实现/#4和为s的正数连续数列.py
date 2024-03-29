'''
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,
他马上就写出了正确答案是100。但是他并不满足于此,他在想究
竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,
他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
'''
def finds(s):
	if s < 1:
		return None
	if s == 1:
		return 1

	start = 1
	end = 2
	result = []
	while start <= (s//2):
		count = sum(range(start,end))
		if count == s:
			result.append(list(range(start,end)))
			start += 1
		elif count < s:
			end += 1
		else:
			start += 1
	return result

result = finds(100)
for i in result:
	print(i)