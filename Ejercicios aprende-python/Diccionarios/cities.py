#entrada de cadena:
cinfo = 'Adeje : 49_270;La Orotava:42_434;Los Silos:4644;Santa Úrsula:15_361;Tegueste:11_359'
#salida: cities, diccionario pero sin los _
lista = cinfo.split(';')
cities = {}
for i in lista:
	r = i.split(':')
	cities[r[0]] = int(r[1])
print(cities)