# Escribir un programa, que dado un arreglo
# devuelva como resultado un nuevo arreglo 
# con cada numero al cuadrado

datos = [1,2,3,4,5,6,7,8,9]

cuadrados = []

for dato in datos:
    cuadrados.append(dato ** 2)

print(cuadrados)

datos.append(10)
print(datos)
datos.remove(1)
print(datos)
print(len(datos))