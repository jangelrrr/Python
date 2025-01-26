# ******************
# ÁREA DE UN CÍRCULO
# ******************


def run(radius: float) -> float:
    #pi*r2
    area = 3.14 * (radius**2)

    return area


if __name__ == '__main__':
    run(4)