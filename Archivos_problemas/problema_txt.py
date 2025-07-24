# 2 listas, una con nombres y  con apellidos
nombres = ["Ana", "Luis", "Pedro","María","Juan"]
apellidos = ["Gómez", "Pérez", "López", "Martínez", "Sánchez"]

# Registrar esta información en un archivo de texto de forma óptima
with open("Archivos_problemas\\nombres_apellidos.txt", "w", encoding="UTF-8") as arch:
    arch.write("Los datos son:\n")
    for n, a in zip(nombres, apellidos):
        arch.write(f"Nombre: {n}\nApellido: {a}\n-----\n")