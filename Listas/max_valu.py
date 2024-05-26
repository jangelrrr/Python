#buscar el valor maximo, sin usar min,max, ni sorted
#entrada: [-11, -10, -6, 15, -1], resultado 15
num =  [-11, -10, -6, -15, -1]
m = -100
for n in num:
	if n > m:
		m = n
print(m)