i = 1
while i <= 9:
    if i % 2 == 0:
        i += 1
        continue        # pares: salta el print
    print("Impar:", i)
    i += 1