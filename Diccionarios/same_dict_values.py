items = {1: 'a', 2: 'a', 3: 'a', 4: 'a'}
#salida: all_same, comprobar si todos los valores son iguales, True o False
all_same = True
v = list(items.values())
if items == {}:
    all_same = False
else:
    val = v[0]
    for i in v:
        if i == val:
            continue
        else:
            all_same = False
            break
print(all_same)