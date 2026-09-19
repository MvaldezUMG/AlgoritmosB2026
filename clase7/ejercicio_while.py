# Crear un programa que devuelva el promedio de N cantidad de notas ingresadas
# finalizar el programa cuando la nota ingresada sea negativa

'''
Tabla de pruebas
Entradas         Salida
3,4,5,-1            4
-1                  Ninguna
7,3,5,5,-2          5
'''

valor = float(input("Ingrese una nota\n"))

suma = 0
cantidad_de_notas=0
while valor >=0:
    suma = suma + valor
    cantidad_de_notas +=1
    valor = float(input("Ingrese una nota\n"))

if cantidad_de_notas > 0:
    print("El promedio es " + str(suma/cantidad_de_notas))
else:
    print("No se han ingresado notas")