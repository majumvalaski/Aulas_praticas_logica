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