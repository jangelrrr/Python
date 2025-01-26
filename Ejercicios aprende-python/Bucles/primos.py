# **************
# NÚMEROS PRIMOS
# **************


def run(n: int) -> bool:
    x = [i for i in range(2, n)]
    for g in range(len(x)):
        x[g] = n % x[g]
    if 0 in x:
        return False
    else:
        return True


if __name__ == '__main__':
    run(2)