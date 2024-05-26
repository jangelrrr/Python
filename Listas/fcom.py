#crear una lista por compresión que ejecute la función al rango de numeros
#función: 3x + 2
#resultado: -19 -16 -13 -10 -7 -4 -1
n = 131
x = 134
s = x - n
#if n < 0:
#    x += abs(n)
l = [3 * i + 2 for i in range(n, x+1)]
print(l)
#n, x+1