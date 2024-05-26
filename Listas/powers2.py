#dado un numero entero, crear potencias de 2
#desde 0 hasta dicho valor, inclusive
#se puede con listas por comprension
#entrada: 2, salida: [1, 2, 4]
n = 2
l = [2 ** i for i in range(0, n+1)]
print(l)