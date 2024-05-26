# **********************
# PIEDRA, PAPEL O TIJERA
# **********************


def run(choice1: str, choice2: str) -> int:
    ch1 = choice1.lower()
    ch2 = choice2.lower()
    if ch1 == 'piedra' and ch2 == 'papel':
        return 2
    elif ch1 == 'papel' and ch2 == 'tijera':
        return 2
    elif ch1 == 'tijera' and ch2 == 'piedra':
        return 2
    elif ch1 == 'papel' and ch2 == 'piedra':
        return 1
    elif ch1 == 'tijera' and ch2 == 'papel':
        return 1
    elif ch1 == 'piedra' and ch2 == 'tijera':
        return 1
    elif ch1 == ch2:
        return 0


if __name__ == '__main__':
    run('piedra', 'PAPEL')