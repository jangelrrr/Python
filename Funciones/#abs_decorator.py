#abs_decorator
#escriba un decorador llamado fabs() que convierta a su valor absoluto los dos primeros parametros de la funcion que decora
#y devuelva el resultado de aplicar dicha función a sus dos argumentos. aplique este decorador a la función fprod() que es el punto
#de entrada del programa
#podria extender el decorador para que tuviera en cuenta un numero indeterminado de argumentos posicionales?
a = -3
b = 7
def fabs(func):
    def wrapped(value1, value2):
        j = abs(value1)
        g = abs(value2)
        return func(j, g)
    return wrapped

@fabs
def fprod(x, y):
    return x * y
    
print(fprod(a, b))
