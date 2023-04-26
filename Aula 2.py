print('Teste')

#O somatório dos 5 primeiro numeros inteiros e positivos
res = 1 + 2 + 3 +4 + 5
print(res)

#A media entre 23, 19 e 31
res = (23+19+31)/3
print(res)

#O numero de vezes que 73 cabe em 403
res = 403//73
print(res)

#A sobra quando 403 é dividido por 73
res = 403%73
print(res)

#Atribuir o valor inteiro 3 a variavel "a"
a = 3
print(a)
#Atribuir o valor 4 a variavel "b"
b = 4
print(b)
#Atribuir a variavel "c"o valor da expressao a*a + b*b
c = a*a + b*b
print(c)

#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto (exercício da apostila - aula 2)
p = float(input('Qual é o preço do produto que está vendendo?'))
d = float(input('Qual o desconto?(entre 0 a 100)%'))
pf = p - p*(d/100)

print('O valor final do produto com desconto de {}% é {}'.format(d, pf))

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00/dia e R$0,15 por km rodado.
km = float(input('Quantos km você rodou com o carro?'))
d = int(input('Quantos dias você ficou com o carro?'))

pkm = km*0.15
pd = d*60

pf = pkm + pd

print('Depois de {} dias com o carro e depois de ter rodado {} km, o valor total a pagar é {}'.format(d, km, pf))

#Crie uma variavel de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string digitada. Imprima na tela somente os dois ultimos caracteres da segunda variavel do tipo string.
a = ('Essa frase é um teste1')
tamanho = len(a)
print(tamanho)

b = a[0:11]
print(b)
print(b[-2:])
