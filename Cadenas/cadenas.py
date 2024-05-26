especiales = "Es un salto de línea\n y esto es un tabulador\t y también puedes poner unas comillas \'simples\' o una barra \\ invertida"
modo_raw = r'Con un\nsalto de linea'
sinmodo_raw='Con un\nsalto de linea'
print(especiales, modo_raw , sinmodo_raw, sep='|', end='$')
name = input('Introduzca su nombre:') #ese será el texto que aparezca y lo que entre se almacenará en name
#las cadenas se pueden sumar y multiplicar
a = 'Se puede'
b = 'sumar'
c = 'y multiplicar'
len(a)
'mu' in c #True
'mu' not in c #False
a.startswith('Se') #True, empieza con Se
a.endswith('Se') #False, no acaba con Se
a.find('pu') #3, devuelve el indice de la primera letra
#lo mismo hace a.index('pu') solo que en caso de no estar las letras, find devolverá -1
a.count('e') #3, cuenta la o las letras
print (a + ', ' + b)
print (c * 3) 
g = 'Quien mal anda mal acaba'
g.replace('mal', 'bien', 1) # 'Quien bien anda mal acaba'
#si no le pones el tercer argumento, cambiará todos
#AÑADIR LO QUE TENGA DE INDEXAR CADENAS
#AÑADIR CAPITALIZE, UPPER, LOWER
#.title (pone todas las palabras con la primera mayuscula)
#.swapcase (pone las mayusculas, minusculas y viceversa)
d = c[2:9:2] #mlil, el ultimo dos indica los saltos
serial = '\n\t    \n  251558542555    \n\t    \t'
serial.strip() # limpia todo 251558542555
serial.strip('\t') #o limpia lo que indiques
#variaciones lstrip por la izquierda y rstrip por la derecha
'R2D2'.isalnum() #True, todos los caracteres son alfanumericos
'R2D2'.isnumeric() #False, todos son numericos
'a-b c'.isalpha() #False, todos son letras (hay guiones y espacios)
#.isupper(), .islower(), .istitle() detecta si son todo mayusculas, minusculas, o las primeras mayusculas
print(f'Y {a} utilizar {b} {{incluido {c} dentro}}') #f-strings, 'Y Se puede utilizar sumar {incluido y multiplicar dentro}'
#tambien puedes añadir formato: ancho de texto, numero de decimales, tamaño de la cifra, alineación,....
f'{text1:<7s}|{text2:-^11s}{text3:>7s}'
#alineación a la izqda, centrado pero rodeado de guiones, alineación dcha
#tambien podemos dejar el nombre de la variable con un igual
f'{serie=}' #"serie='The Simpsons'"
#e incluso rebanados y operaciones
f'{serie[4:]}' f'{num1 / num2=}'
