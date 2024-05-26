items = [['Episode IV - A New Hope', 'May25', 1977, 'George Lucas'], ['Episode V - The Empire Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]]
#salida: unpack_items, las claves son los primeros elementos como cadenas y los valores los restantes, como lista
unpack_items = {}
for i in items:
    unpack_items[i[0]] = i[1:]
print(unpack_items)