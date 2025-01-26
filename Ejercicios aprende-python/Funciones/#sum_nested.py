#sum_nested
#dada una lista, o listas de listas, de enteros, sumar sus valores con una recursiva
items = [1,[2,4],5,[6,[7,8]]]
def sum(items, n = 0):
    for i in range(len(items)):
        if type(items[i]) == list:
            n = sum(items[i], n)
        else:
            n += items[i]
    return n
print(sum(items))
#salida: _sum: int: 33