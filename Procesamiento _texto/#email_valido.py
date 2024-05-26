#email_valido
import re
texto = 'email77@google.com'
regex =r'\b\w+@\w+\.\w+\b'
m = re.fullmatch(regex,texto)
print(m)