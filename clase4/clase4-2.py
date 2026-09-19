nota = int(input("Ingresa tu nota (0-100): "))

'''
Tabla de pruebas:
Entrada  Salida
90       A
80       B
70       C
60       D
59       F
'''

if nota >= 90:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
else:
    letra = "F"

print("Tu calificación es:", letra)