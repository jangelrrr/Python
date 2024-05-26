#indicar si una lista todos los elementos son iguales
#True o False
lista = [1, 1, 1, 1]
for i in range(len(lista)):
	if lista[i] != lista[0]:
		r = False
		break
	else:
		r = True
print(r)