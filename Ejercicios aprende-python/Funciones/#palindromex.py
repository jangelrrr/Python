#palindrome
#funcion que indique si una cadena es palindromo, que se lee igual de dcha a izqda, que al reves
text = 'Yo dono rosas oro no doy'
def palindrome(text:str)->bool:
	txt = text.lower()
	sin_espacios = ''
	for i in range(len(txt)):
		if txt[i] == ' ':
			continue
		else:
			sin_espacios += txt[i]
	al_reves = ''
	i = len(sin_espacios)-1
	while i > -1:
		al_reves += sin_espacios[i]
		i -= 1
	return (al_reves == sin_espacios)
print(palindrome(text))

#salida: palindrome_text