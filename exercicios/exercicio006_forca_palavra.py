"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'perfune'
letras_acerto = ''
tentativas = 0
flag_letra_vazia = None
flag_letra_dupla = None
flag_nao_alpha = None
flag_acerto = None
flag_erro = None

while True:
    
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acerto:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('---'*10, '\n')

    if palavra_formada == palavra_secreta:
        print(f'VOCÊ GANHOU! A palavra era {palavra_secreta.upper()}.')
        print(f'Você precisou de {tentativas} tentativas para acertar.')
        flag_acerto = None
        newgame = input('[Q] para sair ou ENTER para jogar novamente: ').lower()
        if newgame == 'q':
            os.system('clear')
            break
        else:
            letras_acerto = ''
            tentativas = 0
            os.system('clear')
            continue

    if tentativas == 0:
        print('Bem-vindo à PALAVRA-SECRETA. Você precisa descobrir a palavra abaixo antes das suas vidas acabarem.\n')
    elif flag_letra_vazia:
        print('Você não digitou nenhuma letra. Tente novamente!\n')
        flag_letra_vazia = None
    elif flag_letra_dupla:
        print('Você digitou mais de uma letra, tente novamente!\n')
        flag_letra_dupla = None
    elif flag_nao_alpha:
        print('Parece que você não digitou uma letra. Números e caractéries não valem!\n')
        flag_nao_alpha = None
    elif flag_acerto:
        print('Você ACERTOU! Continue tentando até completar a palavra.\n')
        flag_acerto = None
    elif flag_erro:
        print('Você ERROU! Continue tentando até completar a palavra.\n')
        flag_erro = None
    
    print('Palavra secreta: ', palavra_formada, '\n')

    letra_digitada = input('Digite apenas uma letra: ').lower()
    tentativas += 1

    if len(letra_digitada) == 0:
        flag_letra_vazia = True
        os.system('clear')
        continue
    elif len(letra_digitada) > 1:
        flag_letra_dupla = True
        os.system('clear')
        continue
    elif not letra_digitada.isalpha():
        flag_nao_alpha = True
        os.system('clear')
        continue

    os.system('clear')

    if letra_digitada in palavra_secreta:
        letras_acerto += letra_digitada
        flag_acerto = True
    else:
        flag_erro = True