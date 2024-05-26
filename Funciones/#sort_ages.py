#sort_ages
#entrada, lista con diccionarios, con nombre y edad, crear función para ordenar la lista por el campo age, utilizar sorted()
people = [{'name': 'DeRozan', 'age': 33}, {'name': 'Lonzo', 'age': 34}, {'name': 'Beverly', 'age' : 36}]
def run(people):
    speople = list(sorted(people, key= lambda x: x['age']))
    return speople
print(run(people))