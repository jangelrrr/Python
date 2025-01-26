#eliminar numeros duplicados de una lista
#pero sin alterar el orden de los demas
lista = [1, 0, 0, 0, 1, 2, 3, 1, 1]
i = 0
while i < len(lista):
	if lista[i] in lista[i+1:len(lista)]:
		lista.remove(lista[i])
	else:
		i += 1
print(lista)