personas = ["maria","juan","esteban","david", "kenia", "kevin"]

valor = input("Ingrese el nombre a buscar\n")

encontrado = False
# Busqueda secuencial
for persona in personas:
    if persona == valor:
        encontrado = True
        break

if encontrado:
    print("La persona esta en la lista")
else:
    print("Persona no encontrada")