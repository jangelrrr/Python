values = [False, False, False]
oper = 'and'
if oper.startswith('a'):
    result = values[0] and values[1] and values[2]
else:
    result = values[0] or values[1] or values[2]
print(result)