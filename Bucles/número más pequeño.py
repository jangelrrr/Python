def my_min(*args):
	min_val=args[0]
	for i in args:
		if i < min_val:
			min_val=i
	return min_val

print(my_min(8,10,12,22,2))