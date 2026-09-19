''' Escribir un programa que pidas las notas 
de 20 alumnos y calcule el promedio
'''
CANTIDAD_DE_NOTAS = 3
acumulado = 0


for n in range(CANTIDAD_DE_NOTAS):
    nota = float(input("Ingrese la nota: \\"))
    acumulado = acumulado + nota


promedio = acumulado / CANTIDAD_DE_NOTAS
print("El promedio es")
print(promedio)