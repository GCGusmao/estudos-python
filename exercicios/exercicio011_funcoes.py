#  Exercício com funções

#  Crie uma função que multiplica todos os argumentos
#  não nomeados recebidos
#  Retorne o total para uma variável e mostre o valor
#  da variável.

def multiplicacao(*args):
    total = 1
    for valores in args:
        total *= valores
    return total

numeros = 1, 2, 3, 4, 5, 6

resultado = multiplicacao(*numeros)
print(resultado)


#  Crie uma função que fala se o número é par ou impar
#  Retorne se o número informado é par ou impar.
#

def verificacao(x):
    resultado = ''
    if (x % 2) > 0:
        resultado = 'impar'
    else:
        resultado = 'par'
    return resultado

x = input('Digite o número que quer verificar: ')

try:
    x = int(x)
except Exception:
    print(f'Erro desconhecido. "{x}" pode não ser um número.')

resultado = verificacao(x)

print(f'Seu valor {x} e {resultado}.')