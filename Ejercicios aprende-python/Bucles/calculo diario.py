def calcular(f,t,e):
    x = round ((e*0.85), -1)
    b = int(f + t + e)
    if t == 0:
        a = int(f + x)
        i = x / 1.21
    elif e == 0:
        a = b
        i = t / 1.21
    
    return (a, b, i)

f = int(input())
t = int(input())
e = int(input())
print (calcular(f,t,e))