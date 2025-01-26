# *******************************
# PRODUCTO ACUMULADO EN CUADRADOS
# *******************************


def run(n: int) -> int:
    result = 1
    for i in range(1,n+1):
        result = i ** 2 * result
    return result


if __name__ == '__main__':
    run(1)