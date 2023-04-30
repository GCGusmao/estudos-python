#
# Calculadora em Python.
#

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# Neste caso, substituímos qualquer erro pelo bloco de código abaixo.

try:
    num1 = float(num1)
    num2 = float(num2)

    print('')
    print(f'Seu resultado é: {num1 + num2}')

except:
    print('')
    print('Os valores inseridos não são válidos.')
