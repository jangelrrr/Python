to_give_back = 0
available_currencies = [5, 2]
#salida: money_back, diccionario {5: 4}
#sacar el numero de billetes o monedas que hay que dar para el cambio
#empezando por el maś grande, si es imposible sería None, y si el dinero es 0, diccionario vacio
available_currencies.sort(reverse=True)
money_back = {}
while to_give_back > available_currencies[-1]:
	for i in range(len(available_currencies)):
		n = 0
		while to_give_back >= available_currencies[i]:
			to_give_back -=  available_currencies[i]
			n += 1
		if n != 0:
			money_back[available_currencies[i]] = n
if to_give_back != 0:
	print(None)
else:
	print(money_back)