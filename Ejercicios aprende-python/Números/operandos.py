# 0 o negatvo es false y numero positivo es true. en este ejemplo al ser el primero true ya no sigue ejecutando el codigo
x = 3 or 4
# aqui si sigue por culpa de and
y = 3 and 0
z = (type(True), "Verdad", 34)
h = "an" < "bio"
g = "an" > "ana"
# es h diferente a g
j = h != g
print (x, y, z, h, g)
label = 30.258
isinstance(label, float)
#pow calcula la potencia, isinstance indica si es el tipo de dato que se da
pow(2, 3)
#las sumas de numeros flotantes no son exactas. hay un modulo en la libreria de matematicas, que te dice si es cercano al resultado
e = 1.1 + 2.2
# da como resultado 3.30000000003
isclose(e, 3.3)
all(x) #indica si todas las variables dan True
callable(print) #indica si es una función que se pueda llamar
not 5 < 7 #not convierte True en False y viceversa
bool(5) #indica si es True o False
x1 or x2 or x3 or.... #en estes casos python buscara en cada valor el que sea correcto, cuando encuentre el correcto, devolverá ese valor y dejará de buscar
x1 and x2 and x3 and... #este caso hace justo lo contrario, buscará un valor falso y devolverá el valor que sea falso. si todos son verdaderos devolverá todos
#tambien funciona con funciones
is_clean and clean_data(data) #la funcion solo se ejecuta si is_clean es verdadero
is_clean or clean_data(data) #la funcion solo se ejecuta si is_clean es falso
number = 5
0 <= number <= 10 #expresiones encadenadas, devolverá true
open_day = "11 AM" if day == "Sunday" else "9 AM"
id(number) #te devuelve la posición en memoria
#para saber si dos variables se refieren al mismo objeto
number is e #aunque las variables tengan el mimo valor, te saldrá False
number = e
number is e #ahora sí dará True, ya que son dos variables que apuntan al mismo objeto
number is not e #dará False
4 in [3, 2, 8, 28]#False
5 not in (5, 2, 58, 8)#False
("j", "i", "f") + ("s", "w", "d")#("j", "i", "f", "s", "w", "d")
3 * [1, 2, 8]#[1, 2, 8, 1, 2, 8, 1, 2, 8]
(variable := expresion)#devuelve el resultado de la expresión y lo almacena en la variable
#ejemplo, así la variable n le valdrá para futuras operaciones
def validate_length(string):
    if (n := len(string)) < 8:
        print (f"Length {n} is too short")
    else:
        print (f"Length {n} is okay")

a < 10 and b > 30#prioridad de las operaciones: exponente, multiplicación/division, suma/resta, comparaciones (==/</is not/in), not, and, or, :=






