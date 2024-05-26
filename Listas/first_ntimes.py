numbers = [2, 3, 5, 3, 2, 1, 8, 2]
nrep = 3
#salida: target_num, que numero se repite las veces que dice nrep
target = {}
target_num = -1
for i in range(len(numbers)):
    if numbers[i] in numbers[i+1:len(numbers)]:
        rep = [o for o in range(len(numbers)) if numbers[o] == numbers[i]]
        target[numbers[i]] = rep
        if len(rep) == nrep:
            target_num = numbers[i]
            break
    
            
print(target_numpy)
