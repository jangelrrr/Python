#consecutive_seqs
#funcion cual es el primer numero que se repite x veces consecutivas, si no existe False
#resolver el problema con recursión
items = [3, 4, 4 ,7, 9]
target_count = 2
def recurse(items, target_count, i=0, r=1) :
	n = len(items)
	if r == target_count:
		return items[i]
	elif i == n-1 or n == 0:
		return False
	if items[i] == items[i+1]:
		return recurse(items, target_count, i+1, r+1)
	else:
		r = 1
		return recurse(items, target_count, i+1, r)

print(recurse(items, target_count))