contador = 0
i = 0
while i<3:
    largura = float(input("Largura:"))
    comprimento = float(input("Comprimento:"))
    area = largura * comprimento
    if area >= 10 and area <= 20:
        contador = contador + 1
    i = i + 1
print("Quantidade:", contador)