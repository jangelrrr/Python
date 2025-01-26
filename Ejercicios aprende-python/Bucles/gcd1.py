#Maximo comun divisor de dos numeros


numeros = [28, 91]
divisores = []
for num in numeros:
  while num != 1:
    for divisor in range(2,100):
       if num % divisor != 0:
         continue
       else:
         divisores.append(divisor)
         break
    num = num/divisor
  divisores.append('+')
sep = divisores.index('+')
div1 = divisores[0:sep]
div2 = divisores[sep+1:len(divisores)-1]
repetidos = []
repetidos2 = []
for numero in div2:
    if numero in div1:
        repetidos2.append(numero)
    else:
        continue 
for numero in div1:
    if numero in div2:
        repetidos.append(numero)
    else:
        continue
gcd_value = 1
for um in range(2,100):
    if repetidos.count(um) < repetidos2.count(um):
        gcd_value *= um ** repetidos.count(um)
    elif repetidos.count(um) > repetidos2.count(um):
        gcd_value *= um ** repetidos2.count(um)
    else:
        gcd_value *= um ** repetidos.count(um)

print(result)