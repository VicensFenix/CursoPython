# Importamos el módulo re para trabajar con expresiones regulares
import re

# Definimos un texto de ejemplo
texto = '''Hola mundo, esto es una prueba 1. ¿Cómo estás?
Esta es la segunda línea.
Esta es la segunda línea.
Y esta es la tercera línea del texto.'''

# Haciendo una búsqueda simple
resultado = re.search("Hola",texto)

# Haciendo una búsqueda con un patrón más complejo
resultado = re.findall("Esta",texto,flags=re.IGNORECASE)

# \d -> busca dígitos númericos del 0 - 9
resultado = re.findall(r"\d", texto)

# \D -> busca TODO MENOS dígitos númericos del 0 - 9
resultado = re.findall(r"\D", texto)

# \w -> busca caracteres alfanuméricos (letras y números)
resultado = re.findall(r"\w", texto)

# \W -> busca TODO MENOS caracteres alfanuméricos (letras y números)
resultado = re.findall(r"\W", texto)

# \s -> busca espacios en blanco (tabulaciones, espacios, saltos de línea)
resultado = re.findall(r"\s", texto)

# \S -> busca TODO MENOS espacios en blanco (tabulaciones, espacios, saltos de línea)
resultado = re.findall(r"\S", texto)

# . - > busca cualquier carácter excepto saltos de línea
resultado = re.findall(r".", texto)

# \n -> busca saltos de línea
resultado = re.findall(r"\n", texto)

# \ - > busca el carácter de escape
resultado = re.findall(r"\\", texto)

# \. -> cancelar caracteres especiales y busca el punto literal
resultado = re.findall(r"\.", texto)  

# Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)

# ^ -> busca el inicio de una línea
# flags=re.MULTILINE permite que ^ busque al inicio de cada línea
resultado = re.findall(r"^Hola", texto, flags=re.MULTILINE)

# $ -> busca el final de una línea
resultado = re.findall(r"línea\.$", texto, flags=re.MULTILINE)

# {n} -> busca exactamente n repeticiones del patrón
resultado = re.findall(r"segunda{2}", texto)

# {n,m} -> busca entre n y m repeticiones del patrón
resultado = re.findall(r"línea{1,2}", texto)

# | -> operador OR, busca uno u otro patrón
resultado = re.findall(r"Hola|mundo", texto)

print(resultado)