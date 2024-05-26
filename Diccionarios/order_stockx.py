stock = {'pen':20, 'cup':11, 'keyring':40}
merch = 'cup'
amount = 12
#salida: available, saber si existe la cantidad amount en stock
if merch not in stock.keys():
    available = False
elif stock[merch] >= amount:
	available = True
else:
	available = False
print(available)