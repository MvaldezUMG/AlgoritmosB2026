#Tabla de pruebas
''' 
Entrada    Salida
6,4,0      6
3,8,4      8
5,6,7      7
1,1,1      1
6,6,3      6
'''

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b and a > c:
    mayor = a
elif b > c:
    mayor = b
else:
    mayor = c

print("El mayor es:", mayor)