print('''------Bem-vindos à calculadora Python!------
\nAqui você poderá utilizar a melhor calculador da sua vida.
\nPara começar, você primeiro deverá escolher as operações a seguir:
\nDigite "1" para escolher operações com adição;
\nDigite "2" para escolher operações com subtração;
\nDigite "3" para escolher operações com divisão;
\nDigite "4" para escolher operações com multiplicação;
\nDigite "5" para escolher operações com potênciação;
\nDigite "6" para escolher operações com raiz;''')
print('---'*10)

operação_01 = input('Qual a operação desejada? ')
if operação_01 != '1' and operação_01 != '2' and operação_01 != '3' and operação_01 != '4' and operação_01 != '5' and operação_01 != '6':
    print('Você não digitou um número do qual foi orientado.')
    exit()
else:
    print('---'*10)
    if operação_01 == '1':
        print('''Sua escolha foi Adição. Favor escolher os números da operação.
        \n''')
        op_01 = input('Escolha o primeiro número a ser somado: ')
        if not op_01.isnumeric():
            print('Você não digitou um número válido. Tente novamente.')
            exit()
        print('---'*10)
        op_012 = input('Escolha o segundo número a ser somado: ')
        if not op_012.isnumeric():
            print('Você não digitou um número válido. Tente novamente.')
            exit()
        print('---'*10)
        op_01 = int(op_01)
        op_012 = int(op_012)
        op_011 = (op_01 + op_012)
        print('O resultado de sua operação é ', op_011)

    elif operação_01 == '2':
        print('''Sua escolha foi subtração. Favor escolher os números da operação.
        \n''')
        op_02 = input('Escolha o número que será subtraído: ')
        if not op_02.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_022 = input('Escolha o número que irá subtrair: ')
        if not op_022.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_02 = int(op_02)
        op_022 = int(op_022)
        op_0222 = (op_02 - op_022)
        print('O total de sua operação é ', op_0222)

    elif operação_01 == '3':
        print('''Sua escolha foi divisão. Favor escolher os números da operação.
        \n ''')
        op_03 = input('Escolha o número que será dividido: ')
        if not op_03.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_033 = input('Escolha o número divisor: ')
        if not op_033.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_03 = int(op_03)
        op_033 = int(op_033)
        op_0333 = (op_03 / op_033)
        print('O total de sua operação é ', op_0333)

    elif operação_01 == '4':
        print('''Sua escolha foi multiplicação. Favor escolher os números da operação:
        \n ''')
        op_04 = input('Escolha o número a ser multiplicado: ')
        if not op_04.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_044 = input('Escolha o número que será o multiplicador: ')
        if not op_044.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_04 = int(op_04)
        op_044 = int(op_044)
        op_0444 = (op_04 * op_044)
        print('O total de sua operação é ', op_0444)

    elif operação_01 == '5':
        print('''Sua escolha foi potênciação. Favor escolher os números da operação:
        \n''')
        op_05 = input('Escolha o número que será irá na operação: ')
        if not op_05.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_055 = input('Digite o expoente da sua potência: ')
        if not op_055.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_05 = int(op_05)
        op_055 = int(op_055)
        op_0555 = (op_05 ** op_055)
        print('O valor de sua operação é ', op_0555)

    elif operação_01 == '6':
        print('''Sua escolha foi raiz. Favor escolher os números da operação:
        \n''')
        op_06 = input('Escolha o primeiro número de sua operação: ')
        if not op_06.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_066 = input('Digite o expoente de sua raiz: ')
        if not op_066.isnumeric():
            print('Você não digitou um número válido.')
            exit()
        print('---'*10)
        op_06 = int(op_06)
        op_066 = int(op_066)
        op_0666 = op_06 ** (1/op_066)
        print('O valor de sua operação é ', op_0666)

    else:
        print('Por favor, coloque o número correto referente à operação.')