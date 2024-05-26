#entrada dos listas de numeros de la misma longitud
#si la longitud no es la misma, return None
#utilizar funcion zip para mezclarlas y calcular siguiente formula
#v1 * v2 = [4*9 + 3*2 + 8*7 + 1*3] = 101
v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
if len(v1) != len(v2):
	print(None)
lista = list(zip(v1, v2))
result = 0
for n in range(len(lista)):
	r = lista[n]
	result += r[0] * r[1]
print(result)
	