#word_freq
origen = open('/home/jose/data/word_freq/cistercian.txt')
lower_bound = 9
origen_lista = origen.readlines()
lista_palabras = []
for c in origen_lista:
    a = c.strip('\n').split(' ')
    lista_palabras.append(a)
t = 0
while t < len(lista_palabras):
	if type(lista_palabras[t]) == list:
		r = lista_palabras.pop(t)
		n = t
		for i in range(len(r)):
			lista_palabras.insert(n, r[i])
			n += 1
	t += 1
lista_palabras_bajas = []
for i in range(len(lista_palabras)):
	palabra_baja = (lista_palabras[i]).lower()
	lista_palabras_bajas.append(palabra_baja)
palabras = {}
for i in range(len(lista_palabras_bajas)):
	cuenta = lista_palabras_bajas.count(lista_palabras_bajas[i])
	if cuenta >= lower_bound:
		palabras[lista_palabras_bajas[i]] = cuenta
	else:
		continue
print(palabras)