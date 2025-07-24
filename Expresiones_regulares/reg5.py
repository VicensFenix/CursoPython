import re

# 5. Encontrar hashtags en un texto
hashtag_pattern = r'#\w+'
texto = "Me encanta #Python y #MachineLearning"
hashtags = re.findall(hashtag_pattern, texto)  # Devuelve ['#Python', '#MachineLearning']