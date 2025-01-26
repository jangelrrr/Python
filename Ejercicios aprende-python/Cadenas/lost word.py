#buscar palabra, eliminarla y reemplazar
a = 'Tomorrow will be a wonderful day in the beach'
b = 'wonderful'
c = 'great'

def cambiar(a, b, c):
	z = a.find(b)
	x = a[0:z]
	y = a[(z + len(b)):len(a)]
	return x + c + y
	
print(cambiar(a, b, c))