texto = 'pqr3stuvwx'
def sacar(x):
	lista=[int(numero) for numero in texto if numero.isdigit()]
	a = lista[0]
	if len(lista) == 1:
		b = a
	else:
		b = lista[-1]
	return a, b


print(sacar(texto))