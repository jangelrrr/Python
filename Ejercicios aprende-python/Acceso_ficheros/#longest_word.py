#longest_word
origen = open('/home/jose/data/longest_word/java.txt')
lista1 = origen.readlines()
lista2 = []
for c in lista1:
    a = c.strip('\n').split(' ')
    lista2.append(a)
t = 0
while t < len(lista2):
	if type(lista2[t]) == list:
		r = lista2.pop(t)
		n = t
		for i in range(len(r)):
			lista2.insert(n, r[i])
			n += 1
	t += 1
palabra_larga = lista2[0]
for i in range(len(lista2)):
	if len(lista2[i]) > len(palabra_larga):
		palabra_larga = lista2[i]

