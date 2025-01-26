#num_in_interval
#función que indique si un numero esta dentro de un intervalo de números, incluidos los limites
value = 14
lower_limit = 2
upper_limit = 5
def in_range(value, lower_limit, upper_limit)->bool:
    if lower_limit <= value <= upper_limit:
    	return True
    return False
print(in_range(value, lower_limit, upper_limit))    