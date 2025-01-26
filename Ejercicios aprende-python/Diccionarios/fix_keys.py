items = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
#salida: fitems, eliminar los espacios de las palabras clave
fitems = {}
#d = ''.join(cadena.split(' '))
for k, v in items.items():
    esp = ''.join(k.split(' '))
    fitems[esp] = v
print(fitems)
