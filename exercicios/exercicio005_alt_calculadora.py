"""
Esse é um tipo de calcukadora alteranativa ao apresentado no exercício 4.
"""


numero_1 = 0
numero_2 = 0
num_1_float = 0
num_2_float = 0

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite o segundo número: ')

    numeros_validaos = None  #  isto se chama flag, ou seja, estamos marcando uma bandeira neste ponto para verificar um condição futura.
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validaos = True #  neste caso, se ambos os números puderem ser convertidos de str para float, a bandeira mudará para True.
    except:
        numeros_validaos = None

    if numeros_validaos is None:
        print('Um ou mais números são inválidos. Tente novamente.')
        continue #  neste caso, o laço será reinciado, sem continuar os demais operadores.

    break

while True:

    operador = input('Digite um dos operadores válidos [+ - * /]: ')

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('O operador que você digitou não é valido, tente novamente.')
        continue
    elif len(operador) > 1:
        print('Você digitou mais de um operador, tente novamente.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)

    sair = input('Caso deseje sair, digite [s]').lower().startswith('s')  # neste caso, '.islower' converte a str em str minúscula e 'startwith' verififica a condição

    if sair:
        break 