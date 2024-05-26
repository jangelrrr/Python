unsorted_items = {'a':'two', 'b':'one', 'c': 'three'}
#salida: sorted_items
#la salida ha de ser una lista de tuplas con los valores ordenados de forma ascendente
sorted_items = sorted(unsorted_items.items(), key = lambda x: x[1])
print(sorted_items)