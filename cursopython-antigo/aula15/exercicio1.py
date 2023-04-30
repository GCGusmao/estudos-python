
num = input('Favor digitar um número inteiro: ')

while not num.isdigit():   # Verifica se foi digitado um número inteiro. Caso contrário, seguirá no loop abaixo.
    num = input('O número digitado não é válido, tente novamente: ')

print('')
print(f'O número digitado é {num} e foi aceito pelo programa.')
print('')
if (int(num) % 2) == 0:   # Verifica se a divisão por 2 tem resto. Caso tenha, o número é impar. O contrário, será par.
    print(f'Além disto, o número {num} é par.')
else:
    print(f'Além disto, o número {num} é ímpar.')
