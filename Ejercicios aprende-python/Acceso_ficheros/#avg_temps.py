#avg_temps
f = open('/home/jose/data/avg_temps/temperatures.dat')
x = open('/home/jose/data/avg_temps/avg_temps.dat', 'w')
for line in f:
    nums = 0
    lineas = line.strip()
    for n in lineas:
        if n == ',':
            continue
        else:
            nums += int(n)
    avg = round(nums/31, 2)
    result = str(avg)
    x.write(result)
    x.write('\n')
x.close()