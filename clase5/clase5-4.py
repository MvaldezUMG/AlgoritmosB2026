# Crear un programa que pida notas hasta que se ingrese -1
# y calcule el promedio

'''
Analisis:
1. Pedir notas mientras sean <> -1
2. El resultado es el promedio de todas las ingresadas
3. Variables:
    Suma de notas como Entero
    Cantidad de notas como Entero
    Promedio como Real

Tabla de pruebas:
Entrada             Salida
4,4,4,-1             4
-1                   ERROR
0                    0
'''

nota = int(input("Ingrese la nota:\n"))
cantidad_de_notas = 1
suma_de_notas = nota

while nota != -1:
    cantidad_de_notas ++ #Abreviatura que hace cantidad_de_notas = cantidad_de_notas + 1
    suma_de_notas = suma_de_notas + nota
    nota = int(input("Ingrese la nota:\n"))
