n = 3
def hyperfactor(n, x=1):
	if n<1:
		return x
	x *= n ** n
	return hyperfactor(n-1, x)
print(hyperfactor(n))