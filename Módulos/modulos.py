# Importamos un modulo y le asignamos su nombre
# import modulo_saludar as m_saludar

# Importamos una función desde un modulo en especifico
# from modulo_saludar import saludar

# Importamos todo desde un modulo
# from modulo_saludar import *

# Importamos dos funciones desde un modulo en especifico y les asignamos un nombre
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_super_raro

# Creamos las variables con los resultados
saludo = saludar_normal("Carlos")
saludo_raro = saludar_super_raro("Ricardo")

# Mostramos los resultados
print(saludo)
print(saludo_raro)
print(type(saludar_normal))
print(type(saludar_super_raro))

# Para ver las propiedades y metodos de el namespace
# print(dir(namespace))

# Accedemos al nombre de este modulo
# print(__name__)

# Accedemos al nombre del modulo llamado
# print(m_saludar.__name__)