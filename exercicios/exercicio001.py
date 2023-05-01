"""
Peça para o usuário digitar seu nome
Peça para o usuário digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra_1}
        A última letra do seu nome é {letra_2}
Se nada for digitado:
    exiba: "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é \"{nome}\".')
    print(f'Seu nome invertido é \"{nome[::-1]}\".')

    if (' ' in nome):
        print('Seu nome possui espaços!')
    else:
        print('Seu nome não possui espaços!')

    print(f'Seu nome possui {len(nome)} letras.')
    print(f'A primeira letra do seu nome é \"{nome[0]}\"')
    print(f'A última letra do seu nome é \"{nome[-1]}\"')

else:
    print('Desculpe, você deixou campos em branco. :(')