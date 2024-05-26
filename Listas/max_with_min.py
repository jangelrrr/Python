#averiguar el valor maximo de una lista, pero usando la funcion mi
values = [5, 9, -6, 9, -2, -9, -7, 2] 
i = 0
while i < len(values)-1:
    values.remove(min(values))
print(values[0])
