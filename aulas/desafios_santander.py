valor = float(input())

while True:
    if valor > 0:
        print(f'Deposito realizado com sucesso!\n Saldo atual: R$ {valor:.2f}')
        break
    elif valor == 0:
        print('Encerrando o programa...')
        break
    else:
        print('Valor inválido! Digite um valor maior que zero.')
        valor = float(input())
