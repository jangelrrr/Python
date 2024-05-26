#count_vowels_rec
#funcion recursiva que calcule numero de vocales en una cadena
txt = 'Bonito es mejor que feo'
i = 0
n = 0
def count(text, i, n):
	vocales = 'aeiou'
	if i == len(text):
		return n
	elif text[i] in vocales:
		n += 1
	return count(text, i+1, n)
	
print(count(txt, i, n))