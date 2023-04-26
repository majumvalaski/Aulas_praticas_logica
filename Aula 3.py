#Escreva as seguintes expressoes booleanas em linguagem Python:
#O somatorio de 2 com 2 é menor do que 4
print((2 + 2) < 4)

#O valor 7//3 é igual a 1+1
print(7//3 == (1+1))

#A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
print(3*2 + 4*2 == 25)

#A soma de 2, 4 e 6 é maior de que 12
print((2+4+6)>12)

#Se idade é maior que 60, escreva: "Voce tem direito aos beneficios"
idade = int(input("Qual é sua idade?"))
if (idade > 60):
    print("Você tem direito aos beneficios")

#Se dano é maior do que 10 e escudo é igual a 0, escreva: "voce está morto!"
dano = 30
escudo = 0
if (dano and escudo == 0):
    print("Você está morto!")

#Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Voce escapou!
norte = True
sul = False
leste = False
oeste = True
if (norte or sul or leste or oeste == True):
    print("Você escapou!")

#Faça um algoritmo que receba três valores, representando os lados de um triangulo fornecido pelo usuário. Verifique se os valores formam um triangulo e classifique como:
#Equilatero (3 lados iguais)
#Isosceles (2 lados iguais)
#escaleno (3 lados diferentes)

a = float(input('Qual é o valor do lado A?'))
b = float(input('Qual é o valor do lado B?'))
c = float(input('Qual é o valor do lado C?'))

