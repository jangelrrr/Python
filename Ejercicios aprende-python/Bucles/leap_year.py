# **************
# AÑOS BISIESTOS
# **************


def run(year: int) -> bool:
    if year%4 == 0 and not year%100 == 0 or year%400 == 0:
        return True
    else:
        return Falsepy


if __name__ == '__main__':
    run(1900)