#power_recursive
#funcion que calcule x elevado a n usando recursividad, no se puede usar **
x = 5
n = 3
def power(x, n, i=0, y=1):
    if i == n:
        return y
    y *= x
    i += 1
    return power(x, n, i, y)
print(power(x, n))
#salida: result: int: 81
