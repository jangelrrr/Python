#abs_decorator
#escriba un decorador llamado fabs() que convierta a su valor absoluto los dos primeros parametros de la funcion que decora
#y devuelva el resultado de aplicar dicha función a sus dos argumentos. aplique este decorador a la función fprod() que es el punto
#de entrada del programa
#podria extender el decorador para que tuviera en cuenta un numero indeterminado de argumentos posicionales?
a = -3
b = 7
def fabs(func):
    def wrapped(*args):
        lista = (abs(i) for i in args)
        return func(*lista)
    return wrapped

@fabs
def fprod(x, y, z):
    return x * y * z
    
print(fprod(a, b, a))
