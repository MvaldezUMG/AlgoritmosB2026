edad = int( input("edad: ") )
#esperamos s o n
#si usamos un solo simbolo = estamos asignado valor a una variable
permiso = input("tienes permiso: ")

#al usar dos simbolos == estamos comparando
if edad >= 18 and permiso == "s":
    
    print("Puedes entrar")
else:
    print("No puedes entrar")