def method(n1,n2):
	while n2:
		sum = n1^n2
		carry = n1&n2
		n1 = sum
		n2 = carry
	return n1