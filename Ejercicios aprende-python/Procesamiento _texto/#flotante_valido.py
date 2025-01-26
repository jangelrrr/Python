#flotante_valido
#formas de representarlo: 4.0, 4., 04.0, 04., 4.000_000, 4e0
import re
texto = '4e0'
regex = '[0-9]+[.e][0-9_]*'
print(re.fullmatch(regex,texto))