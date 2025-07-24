cadena1 = "Hola,soy,Dalto"
cadena2 = "Bienvenido"

# [Es una función]Se usa para obtener una lista de los atributos y métodos disponibles para un objeto determinado
resul_dir = dir(cadena1)


# Convierte a mayúsculas
mayus = cadena1.upper()


# Convierte a minisculas
minus = cadena1.lower()


# Convierta la primera en mayúscula
prime_mayus = cadena1.capitalize()


#  Método encuentra la primera aparición del valor especifico (Buscamos una cadena en otra cadena, si no hay concidencias no devuelve -1)
busqueda_final = cadena1.find("D")


# Método encuentra la primera aparicicón del valor especifico (Buscamos una cadena en otra cadena, si no encuentra la concidencia nos manda una excepción)
buscamos_index = cadena1.index("D")


# Si es numerico devuelve true si no false
es_numerico = cadena1.isnumeric()


# Si es alfa númerico devuelve true si no false
es_alfanumerico = cadena2.isalpha()


# Devuelve el número de ocurrencias de una subcadena en la cadena dada (Contamos concidencias de una cadena dentro de otra cadena, devuelve la cantidad de conicidencias)
contar_concidencias = cadena1.count("Dalto")


# Cuenta los caracteres de una cadena (Es una función)
contar_caracteres = len(cadena1)


# Verifica si una cadena comienza con cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")


# Verifica si una cadena termina con cadena dada. si es asi devuelve true
termina_con = cadena1.endswith("o")


# Remplaza un valor por otro (Remplaza un pedazo de la cadena dada, por otra dada) Si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("Hola","Adios")


# Separa por el parametro dado (Separar cadenas con la cadena que le pasemos)
cadena_separada = cadena1.split(",")
print(cadena_separada[2])

