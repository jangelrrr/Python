#entrada: cadena con varias palabras
#salida: cadena en minusculas y con las palabras al reves
c = 'Hola que tal'
d = (c.lower()).split(' ')
d.reverse()
d = ' '.join(d)
print(type(d))