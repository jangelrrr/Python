def integral(x: str):
	c = x.find(',')
	a = int(x[c+1:len(x)]) + 1
	b = int(x[0:c]) // a
	return f'{b}x^{a}'

print(integral('3,2'))