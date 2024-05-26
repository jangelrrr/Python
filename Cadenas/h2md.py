def extremos(x):
	n = int(x[2])
	z = x.strip('</h12345>')
	e = n * '#'
	return f'{e}  {z}'

print(extremos('<h4>hola</h4>'))