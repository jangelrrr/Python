def multiply (x:int):
	xy = abs(x)
	y = len(str(xy))
	multi = x * (5 ** y)
	return multi

print (multiply(200))