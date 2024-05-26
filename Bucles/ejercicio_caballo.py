# escribir un programa movimiento caballo, primeiro x suma 1 e y 2
#  e despois o reves, x suma 2 e y 1, hasta que os numeros coincidan coas entradas
x = 7
y = 8
a = 0
b = 0
z = 0
print (f'({a}, {b})', end = ' ')
while a < x and b < y:
    z += 1
    if z%2 == 0:
    	a += 2
    	b += 1
    	print (f'({a}, {b})', end = ' ')
    else:
    	a += 1
    	b += 2
    	print (f'({a}, {b})', end = ' ')
    
    
    
    
