#crear programa que indique si es una url valida
import re
text = 'http:\\www.aprendepython.com'
def validar_url(texto=text):
	regex =  r'ht{2}p:\\w{3}[.][a-z]+[.][a-z]{2,3}'
	m = re.fullmatch(regex, texto)
	if m:
		print('Es una url valida')
		print(m[0])
	else:
		print('No es una url valida')
		return validar_url(texto=input())
validar_url()