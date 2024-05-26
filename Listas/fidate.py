#transforma una entrada de fecha en otro formato
#mes/dia/año, año con 2 cifras a dia-mes-año con 4 cifras
#dos entradas, fecha y año base
#entrada: '12/31/23' y '2000'
#salida: '31-12-2023'
entrada = '12/1/23'
entrada2 = '2000'
lista = entrada.split('/')
mes = lista.pop(0)
lista.insert(1, mes)
for i in range(len(lista)):
	if len(lista[i]) == 1:
		r = lista.pop(i)
		s = '0' + r
		lista.insert(i, s)
año = lista.pop(2)
año2 = str(int(int(entrada2)/100))
año3 = año2 + año
lista.append(año3)
salida = '-'.join(lista)
print(salida)