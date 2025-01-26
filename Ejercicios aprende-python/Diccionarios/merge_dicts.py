d1 = {'a':1, 'b':2}
d2 = {'a':3, 'c':4}
#salida: merged, mezclar diccionarios sin usar los metodos definidos por python
#{'a':3, 'b':2, 'c':4}
for k, v in d2.items():
    d1[k] = v
print(merged)