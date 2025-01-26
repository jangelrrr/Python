def vocales(x):
	ca = x.count('a')
	ce = x.count('e')
	ci = x.count('i')
	co = x.count('o')
	cu= x.count('u')
	cc = ca + ce + ci + co + cu
	return len(x) * cc
	

print(vocales('ordenador'))