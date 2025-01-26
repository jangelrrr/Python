#perfect
#funcion para saber si un numero es perfecto, utilize una función auxiliar para que calcule los divisores
#Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se puede dividir por 1, 2 y 3,
n = 28
def perfect(n):
    divisores = []
    for i in range(1,n):
        if n%i == 0:
            divisores.append(i)
    if sum(divisores) == n:
        return True
    return False
print(perfect(n))

