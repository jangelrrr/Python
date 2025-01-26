#bubble_sort
#funcion que ordene una lista de enteros utilizando el algoritmo de la burbuja
#no modifique la lista de entrada, no utilizar sorted
items = [4,9,1,5]
def bubble(items):
	n = len(items)
	for i in range(n-1):
	           for j in range(n-1-i):
	               if items[j] > items[j+1]:
	               	items[j], items[j+1] = items[j+1], items[j]
	return items
print(bubble(items))
#salida: sorted_items