import pandas as pd
import lxml
origen = pd.read_html('https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma')
df_uno = pd.DataFrame(origen[3])
df_poblacion = df_uno.drop(labels=range(0,24))
df_poblacion = df_poblacion.drop(labels=44)
df_poblacion = df_poblacion.drop(labels=0, axis=1)
df_superficie = pd.DataFrame(origen[4])
df_superficie = df_superficie.drop(labels=19)
df_poblacion = df_poblacion.drop(labels=24)
columnas = {1: 'Comunidad autonoma', 2: 'Poblacion', 3: 'Porcentaje', 4: 'Densidad'}
df_poblacion.rename(columns=columnas, inplace=True)
print(df_poblacion.columns)