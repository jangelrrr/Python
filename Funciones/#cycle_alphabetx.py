#cycle_alphabet
#crear una funcion auxiliar generadora que devuelva el numero de caracteres del alfabeto que se indique
#con desplazamiento circular, si se acaba el alfabeto, que vuelva a empezar
#la función principal debe devolver la conversión a cadena de la llamada a la función auxiliar
max_letters = 30
def run(max_letters):
	def generador(max_letters, i =0, n=0):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		while n != max_letters:
			if i == len(alphabet):
				i = 0
			yield alphabet[i]
			i += 1
			n+= 1
	lista = list(generador(max_letters))
	text = ''.join(lista)
	return text

print(run(max_letters))

