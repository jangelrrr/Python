def may(x, y):
	if x.islower() and y.islower():
		return 1
	elif x.isupper() and y.isupper():
		return 1
	elif not x.isalpha() and y.isalpha():
		return -1
	else:
		return 0
		
print(may('€', 'M'))
		
	