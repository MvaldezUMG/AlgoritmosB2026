#Crear un programa que sume dos numeros pasados por argumentos
#Debemos importar sys para usar los argumentos
import sys

#Usando la palabra clave len() podemos ver el tamaño
if len(sys.argv) != 3:
    print("Uso: python3 argumentos.py <num1> <num2>")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Suma:", a + b)