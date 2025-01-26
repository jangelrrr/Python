# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    arriba=4*x*(180-x)
    abajo=40500-x*(180-x)
    sin = arriba/abajo

    return sin


if __name__ == '__main__':
    run(90)