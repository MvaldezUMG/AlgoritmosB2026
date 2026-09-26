#Crear un programa que dados multiples valores separados por -
# y enviados como argumento, los eleve al cuadrado ejemplo:
# python3 ejercicio.py 1-2-3-4-5 debe devolver 1 4 9 16 25

import sys

if len(sys.argv) < 2:
    print("No se han enviado los valores")
    exit(0) #Terminar el programa
datos = sys.argv[1].split("-")
print(datos)

for d in datos:
    cuadrado = float(d) **2
    print(cuadrado)