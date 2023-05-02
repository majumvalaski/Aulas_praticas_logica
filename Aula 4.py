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

#validando entrada

x = int(input('Digite um valor maior do que zero: '))
while (x<=0):
    x = int(input('Digite um valor maior do que zero: '))
print('Parabens, você acertou!')

#Break
print('Bem-vindo ao labirinto das palavras. Escolha uma para tentar sair')
print('Se acertar a palavra mágica, você sai do labirinto')
while True:
    texto = input('')
    print('Sinto muito, mas ainda não achou a saída')
    if texto == 'sair':
        break
print('Você conseguiu sair do labirinto!')

#Voltando ao inicio do laço com continue
while True:
    nome = input('Qual o seu nome?')
    if (nome != 'Maria'):
        continue
    senha = input('Qual a sua senha?')
    if (senha == 'UnInter'):
        break
print('Acesso concedido.')