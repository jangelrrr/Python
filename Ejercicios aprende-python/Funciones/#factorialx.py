#factorial
n = -1
#crear función que calcule el factorial de ese numero, si es negativo sería None
def factor(n):
	if n < 0:
		return None
	result = 1
	for i in range(1, n+1):
		result *= i
	return result
print(factor(n))