#print(round(1.234567, 3))

#def truncar(n : float, p = 0):
#	i = int(n * 10 ** p) / 10 ** p
#	return i
#numeros = [1.234, 2.451, 5.156]
#media = [truncar(n,1) for n in numeros]
#print(media)
			
#print (truncar(-1234.234567, -2))
import math
def redondear_mitad (n, p = 0):
	multiplicador = 10 ** p
	return math.floor(n * multiplicador + 0.5) / multiplicador
#floor devuelve el entero más bajo, se le suma 0.5 por si el ultimo digito es mayor que 5
#print(redondeo_mitad(1.2449,2))
#pero sigue fallando en negativos
def redondear_desde_cero(n, p = 0):
	redondear = redondear_mitad(abs(n), p)
	return math.copysign(redondear, n)
print(redondear_desde_cero(2.675,2))
