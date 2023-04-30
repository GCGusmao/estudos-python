# Jogo da Forca em Python...

segredo = 'oliveira'
chances = 5
digitadas = []
loop = True

while loop:
    if chances <= 0:
        newgame = input(f'Infelizmente suas chances acabaram! Pressione [enter] para jogar novamente ou [Q] para sair!')
        if newgame == 'q' or newgame == 'Q':
            break
        else:
            chances = 5
            continue
    else:
        letra = input('Digite uma letra: ')

        if len(letra) > 1 or not letra.isalpha():
            print('Nada de trapassear, digite ao menos uma letra e nada mais que uma letra!')
            continue

        digitadas.append(letra)

        segredo_temp = ''
        for letra_secreta in segredo:
            if letra_secreta in digitadas:
                segredo_temp += letra_secreta
            else:
                segredo_temp += '*'

        if segredo_temp == segredo:
            newgame = input(f'Você ganhou!! A letra secreta era {segredo.upper()}! Pressione [enter] para jogar novamente ou [Q] para sair!')
            if newgame == 'q' or newgame == 'Q':
                break
            else:
                chances = 5
                digitadas = []
                continue


        if letra in segredo:
            print(f'Parabéns! A letra {letra} existe na palavra: {segredo_temp}.')

        else:
            digitadas.pop()
            chances -= 1
            if chances > 0:
                print(f'Oh no... Você ainda tem {chances} chances.')
                print('')
