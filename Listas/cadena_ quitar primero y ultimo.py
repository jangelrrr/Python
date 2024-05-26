numbers = '1, 2, 3, 4' 
n = numbers.split(',')
a = len(n)
n.pop(0)
if a > 2:
    n.pop(a-2)
    s = ' '.join(n)
else:
    s = ''
return s