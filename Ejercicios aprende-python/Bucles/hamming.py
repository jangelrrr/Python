# *****************
# DISTANCIA HAMMING
# *****************


def run(text1: str, text2: str) -> int:
    dhamming = 0
    dif = False
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            continue
        elif text1[i] != text2[i]:
            dhamming += 1
    if len(text1) != len(text2):
        dif = True
    return int(-dif) or dhamming

if __name__ == '__main__':
    run('0001010011101', '0000110010001')