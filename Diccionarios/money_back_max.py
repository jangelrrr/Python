to_give_back = 13.5
available_currencies = {5: 20, 2: 1, 0.5: 7}
#salida: money_back, diccionario {5: 3, 2: 2, 1: 1}
#sacar el numero de billetes o monedas que hay que dar para el cambio
#empezando por el maś grande, si es imposible sería None, y si el dinero es 0, diccionario vacio
available_currencies = dict(sorted(available_currencies.items(), reverse=True))
a = list(available_currencies.keys())
c = list(available_currencies.values())
money_back = {}
while to_give_back > a[-1]:
	for i in range(len(a)):
		n = 0
		while to_give_back >= a[i] and n < c[i]:
			to_give_back -=  a[i]
			n += 1
		if n != 0:
			money_back[a[i]] = n
if to_give_back != 0:
	print(None)
else:
	print(money_back)