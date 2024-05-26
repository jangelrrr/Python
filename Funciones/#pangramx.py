#pangram
#funcion que indique si una cadena es un pangrama, si usa todas las letras del alfabeto
text = 'The quick brown fox jumps over the lazy dog'
def pangram(text)->bool:
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	letras = list(alphabet)
	sin_espacios = ''
	for i in range(len(text)):
		if text[i] == ' ':
			continue
		else:
			sin_espacios += text[i]
	for i in sin_espacios.lower():
		if i in letras:
			letras.remove(i)
	if letras == []:
		return True
	return False
print(pangram(text))
	

#salida, pangram_text: True en este caso