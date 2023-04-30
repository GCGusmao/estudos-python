"""
Introdução ao Try / Except
try -> Tenta executar um código
except -> Caso ocorra algum erro na execução do try
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro do número de {numero_str} é {numero_float*2}')
except:
    print('O que você digitou não é um número :(')