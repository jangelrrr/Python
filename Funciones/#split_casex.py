#split_case
#dada una lista con palabras en mayusculas, minusculas y mezcladas
#funcion que divida en dos listas, palabras en mayusculas, palabras en minusculas e ignorar el resto
words = ['AZUL', 'blanco', 'NEGRO', 'Amarillo']
def split(words):
	lower_words = []
	upper_words = []
	for i in words:
		if i.isupper():
			upper_words.append(i)
		elif i.islower():
			lower_words.append(i)
	return lower_words, upper_words
print(split(words))

#salida: lower_words y upper_words