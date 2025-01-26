#entrada-numbers: [4, 2, 9, 7, 1, 8]
#salida-sorted_numbers: ordenar lista en orden ascendente, sin usar sorted
#hacer copia de lista antes de modificarla
numbers = [1,3,5,7,7,2,2,2,4,9,9,9]
e = 0
while e < len(numbers)-1:
    mini = numbers[e]
    for i in range (e+1, len(numbers)):
        if numbers[i] < mini:
            mini = numbers[i]
    numbers.remove(mini)
    numbers.insert(e, mini)
    if mini in numbers[e+1:]:
        indice = [o for o in range(len(numbers)) if numbers[o] == mini]
        indice.pop(0)
        n = 0
        while n < len(indice):
            numbers.pop(indice[n])
            numbers.insert(e, mini)
            n += 1
        e += len(indice)+1
    else:
        e += 1

print(numbers)