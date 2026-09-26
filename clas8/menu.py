"""
Crear un programa con menu que tengas las opciones:
1. Crear alumno
2. Eliminar alumno
3. Listar alumnos
4. Salir
"""

def imprimir_menu():
    print("Elija una opcion:")
    print("1. Crear alumno")
    print("2. ELiminar alumno")
    print("3. Listar alumnos")
    print("4. Salir")

imprimir_menu()
opcion = input("Escriba su respuesta: ")
alumnos = []
while True:
    if opcion == "1":
        alumno = input("Ingrese el nombre del alumno: ")
        alumnos.append(alumno)
    if opcion == "2":
        alumno = input("Ingrese el nombre del alumno: ")
        alumnos.remove(alumno)
    if opcion == "3":
        for a in alumnos:
            print("Nombre: ", a)
    if opcion == "4":
       break
    imprimir_menu()
    opcion = input("Escriba su respuesta: ")




