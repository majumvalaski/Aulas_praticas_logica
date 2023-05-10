import math
print(math.sqrt(9))

from math import sqrt
print(sqrt(9))

notas = [9,7,7,10,3,9,6,6,2]
print(notas.count(7))
notas[-1] = 2
print(notas)
#Maior nota
print(max(notas))
#ordenando
notas.sort()
print(notas)
#media
soma = sum(notas)
n = len(notas)
media = soma/ n
print("Média: {:.2f}".format(media))

import numpy as np
media = np.mean(notas)
print("Média: {:.2f}".format(media))

palavras = ('Abacata', 'Chocolate', 'amor', 'bla', 'carro', 'queijo', 'celular', 'prato', 'nove', 'dez')
for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            vogais.append(letra.lower())

    print(f'As vogais da palavra {palavra} são: {vogais}')
    #print('As vogais da palavra {} são: {}'.format(palavra, vogais))

#jogo de jokenpô
import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x< min) or (x > max)):
        x = int(input(pergunta))
    return x

def vencedor (jogador1, jogador2):
    global empate, v1, v2

    if jogador1 == 1: #pedra
        if jogador2 == 1: #pedra
            empate += 1
        elif jogador2 == 2: #papel
            v2 += 1
        elif jogador2 == 3: #tesoura
            v1 += 1

    elif jogador1 == 2: #papel
        if jogador2 == 1: #pedra
            v1 += 1
        elif jogador2 == 2: #papel
            empate += 1
        elif jogador2 == 3: #tesoura
            v2 += 1

    elif jogador1 == 3: #tesoura
        if jogador2 == 1: #pedra
            v2 += 1
        elif jogador2 == 2: #papel
            v1 += 1
        elif jogador2 == 3: #tesoura
            empate += 1

    resultados = [v1,v2, empate]
    return resultados

#programa principal
print('JOKENPÔ')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('Escolha sua jogada: ', 0, 3)
    if j1 == 0:
        print('Jogo encerrado')
        break

    j2 = random.randint(1,3)
    jogadas.append([j1, j2])
    resultados = vencedor(j1, j2)

    for jogada in jogadas:
        for dado in jogada:
            print(dado, end= ' ')
        print()
#Caso o jogador ja coloque "0" na primeira jogada
if not resultados:
    print('O jogo foi encerrado sem que nenhum resultado pudesse ser calculado.')
else:
    print('Numero de vitorias do jogador 1: {}'.format(resultados[0]))
    print('Numero de vitorias do jogador 2: {}'.format(resultados[1]))
    print('Numero de empates: {}'.format(resultados[2]))

