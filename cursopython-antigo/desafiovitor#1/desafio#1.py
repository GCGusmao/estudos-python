"""
Desafio #1 do Vitor Gayzão Mota. Calculadora top das galáxias
"""

print('Bem vindo à calculadora em Python. Para utilizar a mesma, basta inserir')
print('os valores do calculo e a operação desejada, conforme orientado.')
print('TODOS OS VALORES INSERIDOS DEVEM SER INTEIROS E POSITIVOS.')
print('##################################################################')

print('')

variavel_1 = input('Digite o primeiro valor da sua equação: ')

if not variavel_1.isnumeric():
    print('Infelizmente você digitou um valor inválido e o cógigo se auto-destruirá :(')
    exit()

print('')

operador = input('Digite o operador desejado. As opções são as seguintes. \n'
                 '- Soma: digite [+]\n'
                 '- Subtração: digite [-]\n'
                 '- Multiplicação: digite [*]\n'
                 '- Divisão: digite [/]\n'
                 '- Potenciação: digite [^]\n'
                 '- Raiz: digite [r]\n'
                 'Opção desejada: ')

if operador != '+' and operador != '-' and operador != '*' and operador != '/' and operador != '^' \
        and operador != 'r' and operador != 'R':
    print('Infelizmente você digitou um valor inválido e o cógigo se auto-destruirá :(')
    exit()


print('')

if operador == '^':
    variavel_2 = input('Digite o expoente da sua potência: ')
elif operador == 'r' or operador == 'R':
    variavel_2 = input('Digite o expoente da sua raiz: ')
else:
    variavel_2 = input('Digite o segundo valor da sua equação: ')

if not variavel_2.isnumeric():
    print('Infelizmente você digitou um valor inválido e o cógigo se auto-destruirá :(')
    exit()

print('')

resultado = 0

if operador == '+':
    resultado = float(variavel_1) + float(variavel_2)
elif operador == '-':
    resultado = float(variavel_1) - float(variavel_2)
elif operador == '*':
    resultado = float(variavel_1) * float(variavel_2)
elif operador == '/':
    resultado = float(variavel_1) / float(variavel_2)
elif operador == '^':
    resultado = float(variavel_1) ** float(variavel_2)
elif operador == 'r' or operador == 'R':
    resultado = float(variavel_1) ** (1 / float(variavel_2))

if operador == '^':
    print(f'A equação resultante e sua solução são: {variavel_1}{operador}{variavel_2} = '
          f'{resultado:.2f}.')
elif operador == 'r' or operador == 'R':
    print(f'A equação resultante e sua solução são: {variavel_1}^(1/{variavel_2}) = '
          f'{resultado:.4f}.')
else:
    print(f'A equação resultante e sua solução são: {variavel_1} {operador} {variavel_2} = '
          f'{resultado:.2f}.')

print('')
print('##################################################################')
