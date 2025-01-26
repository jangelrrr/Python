#consecutive_freqs
#la entrada es una lista de enteros repetidos, y un booleano. crear función para si es False, cree una lista llena de tuplas
#con el entero y las veces que se repiten, si es True, crear una cadena, con los datos separados por comas, y los enteros y repetidos
#separados por dos puntos
items = [2,2,1,1,2,2,1,1]
def conse(lista, as_string):
	r = []
	i = 0
	n = 0
	while i < len(items)-1:
		if items[i] == items[i+1]:
			n += 1
			i += 1
		else:
			a = items[i]
			b = n + 1
			c = (a, b)
			r.append(c)
			n = 0
			i += 1
	a = items[i]
	b = n + 1
	c = (a, b)
	r.append(c)
	if as_string:
		lista = []
		s = []
		for i in r:
			a = [str(o) for o in i]
			lista.append(a)
		for i in lista:
			b = ':'.join(i)
			s.append(b)
		c = ','.join(s)
		return c
	else:
		return r
		
print(conse(items, as_string=False))		