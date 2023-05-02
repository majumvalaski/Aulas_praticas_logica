#while

soma = 0
cont = 1

while (cont<=5):
    x = float(input("Digite a {}ª nota: ".format(cont)))
    soma = soma + x
    cont = cont + 1

media = soma / 5
print('A média final foi: {}'.format(media))


while (cont<=5):
    x = float(input("Digite a {}ª nota: ".format(cont)))
    soma += x
    cont += 1

media = soma / 5
print('A média final foi: {}'.format(media))

