import re

# 1. Validar un email
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "usuario@example.com"
if re.match(email_pattern, email):
    print("Email válido")
