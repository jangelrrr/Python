#extract_evens
#funcion que reciba una lista de enteros y devuelva otra con valores pares
values = [1,2,3,4,5,6,7,5,9]
def extract(values):
    result = [i for i in values if i%2==0]
    return result
print(extract(values))