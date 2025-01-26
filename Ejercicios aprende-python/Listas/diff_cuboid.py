#entrada: 2 listas con 3 numeros, datos de dos cubos
#calcular la diferencia de volumenes de los cubos
#volumen del cubo, multiplicar los 3 numeros
a =[25, 40, 3]
b = [30, 37, 2]
ra = 1
rb = 1
for i in a:
	ra *= i
for e in b:
	rb *= e
print(ra-rb)