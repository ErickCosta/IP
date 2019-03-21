contador = 0
i = 0
while i < 2:
    n = input("Informe um número:")
    n = int(n)
    if n >= 30 and n <= 90:
        print("Está no intervalo!")
        contador = contador + 1
    i = i + 1
print("A quantidade de valores entre 30 e 90 é:", contador)