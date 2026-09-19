#pedimos la edad y lo guardamos en una variable
#input es la palabra reservada para pedir datos por consola
#cuando se usa input todos los datos se almacenan como string o cadena de texto
edad = input("ingrese su edad: ")
#convertimos a numero entero
edadEnNumero = int(edad)

#Evaluamos la condicion
if edadEnNumero >= 18:
    #Python require indentacion hacia la derecha para distinguir los bloques
    print("Usted es mayor de edad")
else:
    #Esto se ejecuta si la condicion es falsa
    print("Usted es menor de edad")

print("Programa finalizado")