IVA = 0.12
#valor1 = 100 * IVA + 100
#valor2 = 200 * IVA + 200
#print(valor1, valor2)
def con_iva(precio):
    #return valor * (1 + IVA)
    return precio + precio * IVA
#valor1 = con_iva(100)
#valor2 = con_iva(200)
#print(valor1, valor2)

precio = float(input("Ingrese el precio\n"))
while True:
    if precio <= 0:
        break
    precio_con_iva = con_iva(precio)
    #Al agregar una f antes de " todos los valores en 
    #entre llaves se sustituyen con la variable
    print(f"El precio con iva es {precio_con_iva}")
    precio = float(input("Ingrese el precio\n"))
