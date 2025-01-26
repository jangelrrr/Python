sentence = 'boom'
# salida contar letras
#counter {'b':1, 'o':2, 'm':1}
counter = {}
for i in sentence:
	cont = sentence.count(i)
	counter[i] = cont
print(counter)
