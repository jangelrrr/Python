# *****************
# COMBINANDO TECLAS
# *****************


def run(key1: str, key2: str, key3: str) -> str:
    if key1 == 'CTRL' and key2 == 'ALT':
        if key3 == 'T':
            return 'Open terminal'
        elif key3 == 'L':
            return 'Lock screen'
        elif key3 == 'D':
            return 'Show desktop'
        elif key3 == 'DEL':
            return 'Log out'
    elif key1 == 'ALT' and key2 == 'F2':
        return 'Run console'
    elif key1 == 'CTRL' and key2 == 'Q':
        return 'Close window'
     


if __name__ == '__main__':
    run('CTRL', 'ALT', 'T')