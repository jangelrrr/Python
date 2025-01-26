#con una lista con listas anidadas, eliminar las listas anidadas
#entrada: [0, 10, [20, 30], 40, 50, [60, 70], 80]
#salida: [0, 10, 20, 30, 40, 50, 60, 70, 80]
l = [0, 10, [3, 4], 20, [60, 70], 80]
t = 0
while t < len(l):
	if type(l[t]) == list:
		r = l.pop(t)
		n = t
		for i in range(len(r)):
			l.insert(n, r[i])
			n += 1
	t += 1
print(l)