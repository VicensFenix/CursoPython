import re

# 4. Validar formato de fecha (dd/mm/aaaa)
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
fecha = "25/12/2023"
if re.match(date_pattern, fecha):
    print("Fecha válida")