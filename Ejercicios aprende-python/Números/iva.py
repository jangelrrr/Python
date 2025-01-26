# ***************
# PRECIO SIN IGIC
# ***************


def run(price_with_igic: float, igic: float) -> float:
    rate = 1 + (igic/100)
    clean_price = price_with_igic / rate

    return round (clean_price, 2)


if __name__ == '__main__':
    run(120, 7)