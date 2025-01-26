#dada una lista de listas que forma un cuadrado, sumar diagonal
#las listas de listas tienen que hacer un cuadrado,sino None
#tiene que haber tantos elementos en la lista, como numero de listas
#entrada: [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
#salida : 20
s = [[1, 4, 6, 1], [2, 1, 1, 3], [1, 7, 1, 7], [3, 4, 2, 1]]
def diagonal(l):
	r = 0
	for i in range(len(l)):
		if len(l[i]) != len(l):
			return None
			break
		else:
			r += l[i][i]
	return r
print(diagonal(s))