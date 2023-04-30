
while True:
    num_1 = input('Digite seu primeiro número: ')
    num_2 = input('Digite seu segundo número: ')
    operador = input('Digite seu operador (caso deseje sair, basta digitar [exit]): ')
    print('')

    if operador == 'exit':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Valor inválido, você precisa digitar um número. Tente novamente!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(f'Seu resultado é {num_1 + num_2}.')
    elif operador == '-':
        print(f'Seu resultado é {num_1 - num_2}.')
    elif operador == '*':
        print(f'Seu resultado é {num_1 * num_2}.')
    elif operador == '/':
        print(f'Seu resultado é {num_1 / num_2}.')
    else:
        print('Operador inválido, tente novamente!')
