#saber si una palabra tiene letras repetidas
#buscae por oetra de alphaber y borrsr ess letrs
cadena = 'lu-mberjac-ks'
cade = list(cadena)
for letter in cade:
	if not letter.isalpha():
		cade.remove(letter)
ALPHABET = 'abcdefghijklmnñopqrstuvwxyz'
for letra in ALPHABET:
	if letra in cade:
		cade.remove(letra)
if cade == []:
	print(True)
else:
	print(False)