#palabras_vocal
#buscar en un texto, palabras que empiecen por vocal
import re
texto = 'hola eque al vas or ahi'
regex =r'\b[aeiou]\w+\b'
print(re.findall(regex,texto))