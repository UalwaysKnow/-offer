'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
def power(base,exponent):
	if base == 0:
		return False
	elif base == 1:
		return 1

	if exponent == 0:
		return 1
	elif exponent > 0:
		for i in range(exponent-1):
			base = base * base
		return base
	else:
		for i in range(abs(exponent)-1):
			base = base * base
		base = 1/base
		return base