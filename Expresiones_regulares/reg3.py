import re

# 3. Buscar palabras que comiencen con mayúscula
capital_pattern = r'\b[A-Z][a-z]*\b'
texto = "Python es Genial"
palabras = re.findall(capital_pattern, texto)  # Devuelve ['Python', 'Genial']