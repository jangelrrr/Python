#common_words
entrada = ['Que bonito es vivir', 'bello que es amar', 'Que barato rezar', 'que es barato amar']
#salida a archivo, palabras que se repiten en combinación de dos lineas, .lower
frases = []
repes = []
for i in range(len(entrada)):
    frase = entrada[i].lower().split(' ')
    frases.append(frase)
frase1 = frases[0]
for i in range((len(frases))-1):
	for palabra in frase1:
		frase2 = frases[i+1]
		if palabra in frase2:
			repes.append(palabra)
	frase1 = frase2
	repes.append('\n')
txt = ','.join(repes)
print(txt)
			