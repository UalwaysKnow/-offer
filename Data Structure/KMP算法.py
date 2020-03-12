def Next(s2):
	next = []
	i=0
	j=-1
	next.append(-1)
	while(i<len(s2)-1):#因为next有了第一个值为-1，所以要少循环一次
		if j == -1 or s2[i] == s2[j]:
			i+=1
			j+=1
			next.append(j)
		else:
			j = next[j]
	print(next)
	return next

def KMP(s1,s2):
	next = Next(s2)
	i=0
	j=0
	while i<len(s1) and j<len(s2):
		if j == -1 or s1[i] == s2[j]:
			i+=1
			j+=1
		else:
			j = next[j]
	if j == len(s2):
		return i - len(s2)

s1 = "sdfsfdfsddf"
s2 = "fsfd"
print(KMP(s1,s2))