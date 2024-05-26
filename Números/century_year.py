#calcular siglo a partir de año
def century(x):
	c = x % 100
	if c == 0:
		return (x//100)
	else:
		return (x//100 + 1)

print(century(1601))