#exercicio 3
import numpy as np
cadastro = {'nome':[], 'sexo':[], 'ano':[]}
idades = []
def mulheres_menos30(nome, sexo, idade):
    m_menos30 = []
    if sexo.upper() == 'F' and idade < 30:
        m_menos30.append(nome.upper())
    return m_menos30

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() != 'S':
        print('Digite "S" para sim e "N" para nao')
        continue
    nome = input('Qual é o nome?')
    sexo = input('Qual o sexo? [M/F]')
    if sexo.upper() not in ['M', 'F']:
        print('Digite "M" para masc e "F" para fem')
        continue
    ano = int(input('Qual seu ano de nascimento?'))
    idade = 2023 - ano
    idades.append(idade)
    cadastro['nome'].append(nome.upper())
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)

media = np.mean(idades)
print('Média das idades: {}'.format(media))
mulheres = []
for i in range(len(cadastro['nome'])):
    mulheres += mulheres_menos30(cadastro['nome'][i], cadastro['sexo'][i], 2023 - cadastro['ano'][i])
print('Mulheres abaixo de 30 anos:', mulheres)