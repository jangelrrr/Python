#get_line
#sacar la linea que digan, número, de archivo de texto, la primera linea es 1
origen = open('/home/jose/data/get_line/nasdaq.txt')
line_no = 20
lista1 = origen.readlines()
lista1 = list(map(lambda x: x.strip('\n'), lista1))
print(lista1[line_no-1])
