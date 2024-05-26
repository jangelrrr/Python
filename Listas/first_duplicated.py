#entrada-numbers: [2, 3, 5, 3, 2]
#salida-fdup: primer elemento duplicado, si no return -1, no usar count
numbers = [2, 3, 5]
repe = []
#i = 0
for i in numbers:
	if i in repe:
		print(i)
		break
	else:
		repe.append(i)
if len(repe) == len(numbers):
    print(-1)
