# ******************
# DISTANCIA EUCLÍDEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # d = √((x2 - x1)² + (y2 - y1)²)
    x = (x2-x1)**2
    y = (y2-y1)**2
    distance = (x+y)**0.5
    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)