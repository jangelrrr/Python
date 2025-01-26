#entrada: lista de numeros o cadenas
#entrada2: un numero o cadena de esa lista
#salida: numero o cadena que sigue a la entrada 2
#si no sigue ningún elemento o no existe entrada2 en entrada, None
a = [1, 2, 'Hola', 67, 'gh']
b = 'gh'
def nex(c, n):
	if n not in c:
		return None
	else:
		r = c.index(n)
		if r == len(c) - 1:
			return None
		else:
			return c[r+1]
print(nex(a, b))