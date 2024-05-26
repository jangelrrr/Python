l = [1, '1', 1, '1']
r = 0
for i in range(len(l)):
	if isinstance(l[i], str):
		r += int(l[i])
	else:
		r += l[i]
print(r)