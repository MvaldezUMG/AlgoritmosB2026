'''
Escriba un programa que pida una nota entre 0 y 100, si no estan en ese rango
debe volver a pedir los datos hasta que se introduzca el valor correcto

Tabla de pruebas:
Entrada        Salida
-1             Imprime nota invalida y vuelve a pedir
0              Imprime nota valida
100            Imprime nota invalida
101            Imprime nota invalida y vuelve a pedir

'''

nota = int(input("Nota (0-100): "))

while nota <0 or nota > 100:
    print("Nota invalida, intente de nuevo")
    nota = int(input("Nota (0-100): "))

print("Nota valida:", nota)