'''
Tabla de pruebas
Entrada         Salida
1, 1,1          La suma es: 2
2, 1,1          La resta es: 0
3, 1,1          La multiplicacion es: 1
4, 1,1          La division es 1
4, 1,0          La division entre 0 no esta permitida
5               Programa finalizado
'''
# Aca intencionalmente colocamos true para que el while sea infinito.
while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir ")
    print("5. Salir")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        n1 = float(input("Ingrese un numero: "))
        n2 = float(input("Ingrese otro numero: "))
        print("La suma es: ", n1 + n2)
    if opcion == 2:
        n1 = float(input("Ingrese un numero: "))
        n2 = float(input("Ingrese otro numero: "))
        print("La resta es: ", n1 - n2)
    if opcion == 3:
        n1 = float(input("Ingrese un numero: "))
        n2 = float(input("Ingrese otro numero: "))
        print("La multiplicacion es: ", n1 * n2)
    if opcion == 4:
        n1 = float(input("Ingrese un numero: "))
        n2 = float(input("Ingrese otro numero: "))
        if n2 == 0:
            print("La division entre 0 no esta permitida")
            continue #Se usa continue para que se envie a la proxima iteracion
        print("La division es: ", n1 / n2)
    if opcion == 5:
        # La opcion 5 usa break para terminar el bucle infinito.
        break

print("Programa finalizado")