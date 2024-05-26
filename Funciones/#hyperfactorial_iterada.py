#hyperfactorial
#el hiperfactorial de un numero n, por ejemplo 5 es 5**5 * 4**4 * 3**3 * 2**2 * 1**1
#escribir funcion que calcule eso, notas: n>=1, puede plantear la version iterativa y la version recursiva
n = 3
def hyperfactor(n):
	x = 1
	while n>0:
		x *= n ** n
		n -= 1
	return x
print(hyperfactor(n))
#salida: hyperfactorial: 108