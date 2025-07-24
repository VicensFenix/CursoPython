# Creando diccionarion con dict()
diccionario = dict(nombre="Lucas",apellido="Dalto")

# Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jaajajja"}

# Creando diccionarios con fromkeys() [Es un método] El primer dato es la clave y el segundo valor
# Valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido","edad"])
# Cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"no se") 

print(diccionario["nombre"])