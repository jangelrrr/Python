values =[45, 56, 300, 29, 6, 10, 1100]
i = 1
max_value = values[0]
min_value = values [0]
while i < len(values):
        if values[i] < min_value:
        	min_value = values[i]
        elif values[i] > max_value:
        	max_value = values[i]
        i += 1
print(min_value)
print(max_value)