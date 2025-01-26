# *************************
# ECUACIÓN DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
    raiz=(b**2-4*a*c)**0.5
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
 #   x1 = x2 = 'output'

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)