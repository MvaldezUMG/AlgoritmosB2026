#Crear un programa que dado un nombre, genere un correo institucional 
#automaticamente, por ejemplo Marco Tulio Valdez debe resultar en
# marco.tulio.valdez@miumg.edu.gt

#nombre = input("Ingrese su nombre: ")

def generar_correo(nombre):
    identificador = nombre.replace(" ", ".").lower()
    dominio = "@miumg.edu.gt"
    return identificador + dominio
 
#print("el correo es: ", generar_correo(nombre))

#RETO: Cambiar este programa a un bucle infinito que pida
# nombres y los vaya almacenando, si detecta un duplicado
# debe agregar un numero