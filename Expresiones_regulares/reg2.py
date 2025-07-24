import re

# 2. Extraer todos los números de un texto
number_pattern = r'\d+'
texto = "Hay 3 manzanas y 5 naranjas"
numeros = re.findall(number_pattern, texto)  # Devuelve ['3', '5']