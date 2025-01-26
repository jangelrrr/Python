#read_csv
superior = []
f = open('/home/jose/data/read_csv/pokemon.csv')
x = f.read().strip('\n').split()
titulos = x.pop(0).split(',')
for i in x:
    o = i.split(',')
    di = {}
    for a, b in zip(titulos, o):
        if b.isdecimal():
            b = int(b)
        if b == '':
            b = None
        if b == 'True':
            b = True
        if b == 'False':
            b = False
        di[a] = b
    superior.append(di)

print(superior)




