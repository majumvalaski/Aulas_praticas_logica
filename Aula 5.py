def soma(x=0, y=0,z=0):
    """
    Funçao que soma até 3 valores inteiros
    :param x: int
    :param y: int
    :param z: int
    :return: soma dos valores inteiros
    """
    return x+y+z

print(soma(3,2))
#help(soma)

#exercicio 1
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while(x < min or x > max):
        x = int(input(pergunta))
    return x
def fatorial (x):
    fat = 1
    if x == 0:
        return fat
    else:
        for i in range(1, x +1):
            fat = fat *i
        return fat

x = valida_int('Digite um numero para calcular a fatorial: ', 0, 99)
print('{}! = {}'.format(x, fatorial(x)))


#exercicio 2 - criando arquivo txt
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criaçao do arquivo')
    else:
        print('Arquivo {} criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao leo o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo (nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{} --- {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo Localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastro')
    print('3 - Sair')

    op = valida_int('Escolha a opçao desejada: ', 1, 3)
    if op == 1:
        print('Opçao de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opçao de lista cadastro selecionada...\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando o programa...\n')
        break



