marks = {'Ana':4, 'Domingo':7, 'Eva':5, 'Alvaro':3, 'Juan':8, 'Belen':1}
#salidas: passed los que aprobaron, y con los nombres en mayusculas
#failed, los que suspendieron con el nombre en minusculas
passed = {}
failed = {}
for name, note in marks.items():
    if note < 5:
        failed[name.lower()] = note
    elif note >= 5:
        passed[name.upper()] = note
print(failed)