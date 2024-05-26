#entrada: cadena con varias palabras
#salida: lista, con palabras separadas junto con el numero de letras separado con un espacio
c = 'Hola que tal'
l = c.split(' ')
for i in range(len(l)):
	s = len(l[i])
	l[i] = l[i] + ' ' + str(s)
print(l)