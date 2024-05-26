imoves = 'A1,B4,A-2,A7,B1,C4'
#salida: inventory = diccionario
#las letras son articulos, y los numeros el inventario(que puede ser negativo)
#sacar eso en un diccionario
#no siempre es a, b, c
inven = imoves.split(',')
inventory = {}
for i in inven:
	if i[0] in inventory.keys():
		inventory[i[0]] += int(i[1:])
	else:
		inventory[i[0]] = int(i[1:])
print(inventory)
