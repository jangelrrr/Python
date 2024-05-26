#entrada-n: 3
#salidas- left_side, right_side: 36, 36
#para entrada 3, uno es (1+2+3)**2, salida2 1**3+2**3+3**3
n = 3
i = 1
left_side = 0
right_side = 0
while i < n+1:
	l = i**3
	right_side += l
	left_side += i
	i += 1
left_side **= 2
print(right_side)
