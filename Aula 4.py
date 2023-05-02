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


#Realize a sequencia de print com for e while
#a) Inteiros de 3 até 12, com 12 incluso
for i in range (3, 13):
    print(i)

x = 3
while (3 <= x <= 12):
    print(x)
    x += 1
#b)Inteiros de 0 até 9, excluindo 9, com passo de 2
x = 0
while (0 <= x < 9):
    print(x)
    x += 2

for i in range (0, 9, 2):
  print(i)

# CALCULADORA
print('CALCULADORA')
print('+ Adiçao')
print('- Subtraçao')
print('* Multiplicaçao')
print('/ Divisao')
print('Pressione outra tecla para sair')

op = input('Qual operaçao voce quer fazer?')
if op == '+' or op == '-' or op == '*' or op == '/':
    a = float(input('Digite o primeiro valor'))
    b = float(input('Digite o segundo valor'))

while (op != 's'):

    if op == '+':
        res = a + b
        print('o resultado de {} + {} = {}'.format(a, b, res))

    elif op == '-':
        res = a - b
        print('o resultado de {} - {} = {}'.format(a, b, res))

    elif op == '*':
        res = a * b
        print('o resultado de {} * {} = {}'.format(a, b, res))

    elif op == '/':
        res = a / b
        print('o resultado de {} / {} = {}'.format(a, b, res))

    else:
        print('Operaçao invalida')

    op = input('Qual operaçao voce quer fazer?')
    if op == '+' or op == '-' or op == '*' or op == '/':
        a = float(input('Digite o primeiro valor'))
        b = float(input('Digite o segundo valor'))

print('Encerrando o programa...')