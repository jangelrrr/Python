#PYCHECK WC
words = 0
lineas = 0
x = ''
with open('/media/jose/Drive/prueba') as f:
    for line in f:
        x += line
        lineas += 1
        if len(line) != 1:
            words += 1
            for letter in line:
                if letter == ' ':
                    words += 1
        else:
            continue
bytes = len(x.encode('utf-8'))
print(words, lineas, bytes)