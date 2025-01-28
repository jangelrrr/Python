lista_nutr = [('Cornstarch',
  {'calories': 381,
   'total_fat': 0.1,
   'protein': 0.26,
   'carbohydrate': 91.27,
   'sugars': 0.0}),
 ('Nuts, pecans',
  {'calories': 691,
   'total_fat': 72.0,
   'protein': 9.17,
   'carbohydrate': 13.86,
   'sugars': 3.97}),
 ('Eggplant, raw',
  {'calories': 25,
   'total_fat': 0.2,
   'protein': 0.98,
   'carbohydrate': 5.88,
   'sugars': 3.53}),
 ('Teff, uncooked',
  {'calories': 367,
   'total_fat': 2.4,
   'protein': 13.3,
   'carbohydrate': 73.13,
   'sugars': 1.84}),
 ('Sherbet, orange',
  {'calories': 144,
   'total_fat': 2.0,
   'protein': 1.1,
   'carbohydrate': 30.4,
   'sugars': 24.32}),
 ('Cauliflower, raw',
  {'calories': 25,
   'total_fat': 0.3,
   'protein': 1.92,
   'carbohydrate': 4.97,
   'sugars': 1.91}),
 ('Taro leaves, raw',
  {'calories': 42,
   'total_fat': 0.7,
   'protein': 4.98,
   'carbohydrate': 6.7,
   'sugars': 3.01})]
entrada = {'Cauliflower':100, 'Teff': 100, 'Nuts':100}
#los valores son los gramos de cada alimento. la salida será un diccionario con los valores nutricionales totales de los alimentos, si el alimento no existe, la salida será el primer alimento que no existe
dici = {'calories' : 0, 'total_fat' : 0, 'protein' : 0, 'carbohydrate' : 0, 'sugars' : 0}

for i , j in entrada.items():
	faltante = 1
	for o in lista_nutr:
		if i in o[0]:
			faltante = 0
			for e in o[1].keys():
				dici[e] += o[1][e] * (j/100)
	if faltante == 1:
		print(i)
print(dici)