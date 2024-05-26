#sum_matrix
j = open(matrix1_path)
h = open(matrix2_path)
a = j.readlines()
b = h.readlines()
d = []
e = []
for c in a:
    a = c.strip('\n').split(' ')
    d.append(a)
for f in b:
    b = f.strip('\n').split(' ')
    e.append(b)
for linea in d:
    for i, n in enumerate(linea):
        n = int(n)
        linea[i] = n
for linea in e:
    for i, n in enumerate(linea):
        n = int(n)
        linea[i] = n
g = open(result_path, 'w')
c = []
for i in range(len(d)):
	v = []
	for x, y in zip(d[i], e[i]):
		z = str(x + y)
		v.append(z)
	v.append('\n')
	c.append(v)
for i in range(5):
	v = ' '.join(c[i])
	g.write(v)
g.close()
