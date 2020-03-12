def zhuanhuan(s):
	if s is None or len(s)<1:
		return None
	if len(s)==1:
		if s[0] < '0' or s[0] > '9' or s[0] == "+" or s[0] == "-":
			return None
		else:
			return int(s[0])

	s = list(s)
	flag = 1
	if s[0] == '-' or s[0] == '+':
		if s[0] == '-':
			flag = -1
		s.pop(0)
	number = 0

	for i in s:
		if i < '0' or i > '9':
			return None
		else:
			number = int(i) + number*10

	return flag*number

s = '-321'
print(zhuanhuan(s))