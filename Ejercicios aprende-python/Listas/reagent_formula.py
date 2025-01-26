#dada una lista de numeros
#cada numero es un producto quimico, y hay reglas
#Regla 1: El componente 1 y el componente 2 no se pueden seleccionar al mismo tiempo.                 
#Regla 2: El componente 3 y el componente 4 no se pueden seleccionar al mismo tiempo
#Regla 3: El componente 5 y el componente 6 tienen que seleccionarse al mismo tiempo.
#Regla 4: El componente 7 o el componente 8 tienen que seleccionarse (uno de los dos, o los dos)
#la salida es true o false, si se puede juntar o no los numeros que hay en la lista 
l = [2, 3, 5, 6, 8]
def quimi(n):
	match n:
		case n if 1 in n and 2 in n:
			return False
		case n if 3 in n and 4 in n:
			return False
		case n if 6 in n and 5 not in n:
			return False
		case n if 5 in n and 6 not in n:
			return False
		case n if 7 not in n and 8 not in n:
			return False
		case _:
			return True
print(quimi(l))