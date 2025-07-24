# Importando el modulo re para trabajar con expresiones regulares
import re

# Detectamdo un numero CABA y ocultandolo
texto = "Hola Pedro, mi número es: +54 11 4321-4321"

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

remplazo = re.sub(pattern,"(Numero oculto)", texto)
print(remplazo)