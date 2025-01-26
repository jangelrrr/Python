pdata = {'Tokyo':38140000, 'Delhi':26454000, 'Shanghai':24484000, 'Mumbai':21357000}
#salida: avg_data
#calcular porcentaje de población relativo con respecto al total, precision de 3 decimales
d = sum(pdata.values())
avg_data = {}
for k, i in pdata.items():
    avg = round((i/d)*100,3)
    avg_data[k] = avg

    
print(pdata)
