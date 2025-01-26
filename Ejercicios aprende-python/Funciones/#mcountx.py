#mcount
#crear funcion que cuente el numero de veces que aparece un valor (target) en una tupla
#no se puede utilizar count, utilice anotación de tipos y valores por defecto
#documente la función siguiendo el formato Sphinx
items = (1,2,3,1,1,5,6,1)
target = 1
def contar(*items: int, target: int = 1) -> int:
    """La función cuenta el numero de veces que se repite un numero
    :param items: la tupla donde hay que buscar el numero
    :type items: tuple
    :param target: el numero que hay que buscar
    :type target: int
    
    :return: numero de veces que se repite target
    :rtype: int
    """
    n = 0
    for i in items:
        if i == target:
            n += 1
        else:
            continue
    return n
print(contar(*items))
