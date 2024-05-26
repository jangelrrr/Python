items = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
#salida: citems, elimine el contenido de las listas, como valor las listas vacias
citems =  {ke:[] for ke in items.keys()}
print(citems)