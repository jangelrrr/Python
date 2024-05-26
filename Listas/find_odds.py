a = [2, 4, 6, 2]
i = 1
while i < len(a):
    if a[i-1] == a[i]:
        a.pop(i)
    i += 1
e = 0
while e < len(a):
    if a[e] % 2 == 0:
        a.pop(e)
    else:
        e += 1
print(a)