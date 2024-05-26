#pylint:disable= 'inconsistent use of tabs and spaces in indentation (<unknown>, line 27)'
#magic_square
#un cuadrado magico es una matriz cuadrada donde la suma de sus numeros por filas, columnas y diagonales es la misma
#dada una lista de listas; matriz cuadrada; determine si es o no un cuadrado magico
#ayudate de funciones auxiliares y listas de comprensión
#TODO SUMA 15
values = [[4,9,2],[3,5,7],[8,1,6]]
def magic(value):
	tamaño = len(value)
	suma = sum(value[0])
	def columnas(value, tamaño, suma):
	       for o in range(tamaño):
	       	x = sum([value[i][o] for i in range(tamaño)])
			if x != suma:
        		return False
        	return True
	def filas(value, tamaño, suma):
	       for o in range(tamaño):
	       	x = sum(value[o])
	       	if x != suma:
	       		return False
	       return True
	def diagonal(value, tamaño, suma):
		x = 0
		i = 0
		o = tamaño - 1
		while o > -1:
			x += value[i][o]
			o -= 1
			i+= 1
		if x != suma:
			return False
		x = sum([value[i][i] for i in range(tamaño)])
		if x != suma:
			return False
		return True
	return columnas(value, tamaño, suma) and filas(value, tamaño, suma) and diagonal(value, tamaño, suma)
print(magic(values))
        


#salida: True, si la lista está vacia, es True