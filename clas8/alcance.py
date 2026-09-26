TOTAL = 100

def agregar(precio):
    #Toda variable declarada dentro de una funcion
    #solo se puede usar dentro de ella
    subtotal = precio * 1.12
    return subtotal

print(agregar(100))
#print(subtotal)

def variable_global():
    total = 400
    print(total)

variable_global()
print(TOTAL)