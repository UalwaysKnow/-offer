def fanzhuan(s):
	sentence = []
	word = []
	for i in s:
		if i == " " or s.index(i) == len(s) - 1:
			if s.index(i) == (len(s) - 1):
				word.append(i)
			temp = "".join(word)
			sentence.append(temp)
			word = []
		elif i != " ":
			word.append(i)
	sentence = sentence[::-1]
	return " ".join(sentence)

s = 'I have a pet cat.'
print(fanzhuan(s))