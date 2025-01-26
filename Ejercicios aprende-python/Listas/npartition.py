#entrada: lista de numeros
#entrada2: un numero
#salida: lista de listas, donde la primera tenga numeros de la lista menor que entrada2
#y la otra, numeros con mayores o igual que entrada2
a = [1, 2, 3, 4, 5, 7, 8]
b = 6
c = []
d = []
i = 0
while i < len(a):
	if a[i] < b:
		c.append(a[i])
	elif a[i] > b:
		d.append(a[i])
	i += 1
result = [c, d]
print(result)