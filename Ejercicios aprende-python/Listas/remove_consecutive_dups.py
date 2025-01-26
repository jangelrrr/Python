#eliminar elementos duplicados contiguos en una lista
#entrada: [a, b, b, b, c, b]
#salida: [a, b, c, b] con comillas todos obvio
lista = ['a', 'b', 'b', 'c', 'b']
i = 1
while i < len(lista):
      if lista[i] == lista[i-1]:
         lista.pop(i)
      else:
         i += 1
print(lista)