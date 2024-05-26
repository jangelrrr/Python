# ********************************
# RESOLVIENDO UNA OPERACIÓN SIMPLE
# ********************************


def run(num1: int, num2: int, op: str) -> float:
    match op:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            return None

if __name__ == '__main__':
    run(5, 2, '+')