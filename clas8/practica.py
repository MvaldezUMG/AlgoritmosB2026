#Crear una funcion que recibe como argumento una cadena separada por ,
#El primer elemento indica la operacion a realizar, por ejemplo:
# sum,1,2,3 debe devolver 6
# res,1,2,3 debe devolver -4
# mul,1,2,3 debe devolver 6
# div,10,5,2 debe devolver 1
def operar(entrada):
    datos = entrada.split(",")
    resultado = 0
    if datos[0] == "sum":
        for dato in datos:
            resultado += float(dato)
    if datos[0] == "res":
        for dato in datos:
            resultado -= float(dato)
    if datos[0] == "mul":
        for dato in datos:
            resultado *= float(dato)
    if datos[0] == "div":
        for dato in datos:
            resultado /= float(dato)
    return resultado
        