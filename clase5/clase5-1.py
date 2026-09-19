# Crear un programa que pida 5 numeros 
# y devuelva la suma de los numeros

resultado = 0

#Repetir desde 0 hasta 5-1
for n in range(5):
    #Al numero n se le conoce como indice y empieza en 0
    numero = int(input("Ingrese el numero:\n"))
    resultado = resultado + numero

print("La suma es " + str(resultado))