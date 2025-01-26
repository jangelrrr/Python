# *******************
# MÍNIMO DE 3 VALORES
# *******************

def run(value1: int, value2: int, value3: int) -> int:
    if value1 < value2:
         if value1 < value3:
             return value1
         else:
             return value3
    elif value1 > value2:
         if value2 < value3:
             return value2
         else:
             return value3
    else:
         return value1


if __name__ == '__main__':
    run(7, 4, 9)