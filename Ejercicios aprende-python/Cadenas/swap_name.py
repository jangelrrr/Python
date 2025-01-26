def swap(x):
	c= x.find(' ')
	a = x[0:c]
	b = x[c+1:len(x)]
	return f'{b} {a}'

print(swap('Terminator T-800'))