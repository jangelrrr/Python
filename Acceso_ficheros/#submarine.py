#submarine
#se dan movimientos de submarino: distancia, profundidad y litros de combustible
#valor positivo es descender, negativo ascender
#consumo 3 litros por metro de distancia + 2 litros profundidad
#no debe subir de 0, ni debe bajar de 600m
origen = open('/home/jose/data/submarine/route1.dat')
litros = int(origen.readline())
rutas = origen.readline().strip('\n').split(',')
rutas = ['10:10','10:10','10:10','30:-31','7:20','55:11']
rutas_distancia = []
rutas_profundidad = []
for ruta in rutas:
	p = ruta.partition(':')
	rutas_distancia.append(int(p[0]))
	rutas_profundidad.append(int(p[2]))
distancia = 0
profundidad = 0
for x, y in zip(rutas_distancia, rutas_profundidad):
	distancia += x
	litros -= abs(x) * 3
	p = profundidad + y
	if p > 600:
		litros -= (601 - profundidad) * 2
		profundidad = p
		break
	elif p < 0:
		litros -= (profundidad + 1) * 2
		profundidad = p
		break
	else:
		profundidad += y
		litros -= abs(y) * 2
	if litros < 0:
		break
print(distancia, profundidad, litros)	