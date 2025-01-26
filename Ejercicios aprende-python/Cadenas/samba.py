def stri(x):
	y = x.lstrip('/')
	z = y.find('/')
	a = y[0:z]
	b = y[z+1:len(y)]
	return a, b
	
	
	
print (stri('//samba-server/psf/guido'))
	