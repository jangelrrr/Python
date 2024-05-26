#valuerror
#se lanza cuando no podemos convertir str en int, escriba un función getint que lea un valor entero dado por input y lo devuelva
#iterando mientras el valor no sea correcto.
#ejemplo: 'Dame un numero entero: ten', 'No es un entero valido. Vuelva a intentarlo'
#puedes probar también la versión recursiva
def getin(): # manera recursiva
	n = input()
	try:
		entero = int(n)
	except ValueError:
		print('No es un entero valido. Vuelva a intentarlo')
		return getin()
	else:
		print(f'Este es un numero entero: {entero}')
#=====================================
def getin(n = 'Hola'): #manera iterable
	while isinstance(n, int) == False:
			n = input()
			try:
				entero = int(n)
			except ValueError:
				print('No es un entero valido. Vuelva a intentarlo')
			else:
				print(f'Este si es un entero valido: {entero}')
				break
getin()