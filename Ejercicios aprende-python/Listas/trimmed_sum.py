#sumar una lista de numeros, menos el valor maximo y el minimo
n = [6, 2, 1, 8, 10]
i = 1
maxi = n[0]
mini = n[0]
while i < len(n):
	if maxi < n[i]:
		maxi = n[i]
	if mini > n[i]:
		mini = n[i]
	i += 1
n.remove(maxi)
n.remove(mini)
result = sum(n)
print(result)