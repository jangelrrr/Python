words = ['mesa', 'movil', 'barco', 'coche', 'avion', 'bandeja', 'casa', 'monitor', 'carretera', 'arco']
#salida: group_words, agrupar las palabras que tenga la misma letra inicial en un diccionario
#con la letra inicial como palabra clave
ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
group_words = {}
for letra in ALPHABET:
	ps = [p for p in words if p[0] == letra]
	if ps == []:
		continue
	else:
		group_words[letra] = ps
print(group_words)