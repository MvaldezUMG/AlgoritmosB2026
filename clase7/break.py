n = 28
divisor = 2

while divisor < n:
    if n % divisor == 0:
        print("Primer divisor encontrado:", divisor)
        break          # ¡fuera del bucle! a la linea 9
    divisor += 1
print("despues del break")