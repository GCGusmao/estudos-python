"""
Faça uma lista de compras. O usuário pode:
Inserir valores, deletar valores e listar os itens da lista.
Não permita que o programa quebre com indices 
"""

import os

lista = []
item_temp = 0

print('Bem-vindo a lista de compras!\n')
print('*'*50, '\n')

while True:

    menu = input('Escolha [a]dicionar, [d]eletar ou mesmo [l]istar os itens: ').lower()

    if menu == 'a':
        os.system('clear')
        print('Bem-vindo a lista de compras!\n')
        print('*'*50, '\n')
        lista.append(input('Digite o nome do item: '))
        os.system('clear')
        print('Bem-vindo a lista de compras!\n')
        print('*'*50, '\n')
        item_temp = (len(lista)) - 1 
        print(f'Item {lista[item_temp].upper()} adicionado com sucesso!')
    elif menu == 'd':
        try:
            os.system('clear')
            print('Bem-vindo a lista de compras!\n')
            print('*'*50, '\n')
            lista.pop(int(input('Digite o índice que deseja excluir: ')))
        except ValueError:
            os.system('clear')
            print('Bem-vindo a lista de compras!\n')
            print('*'*50, '\n')
            print('Você não digitou um valor válido (inteiro e positivo), tente novamente.')
        except IndexError:
            os.system('clear')
            print('Bem-vindo a lista de compras!\n')
            print('*'*50, '\n')
            print('Você digitou um índice inexistente, tente novamente.')
        except Exception:
            os.system('clear')
            print('Bem-vindo a lista de compras!\n')
            print('*'*50, '\n')
            print('Erro desconhecido, tente novamente.')
    elif menu == 'l':
        os.system('clear')
        print('Bem-vindo a lista de compras!\n')
        print('*'*50, '\n')
        if len(lista) == 0:
            print('Sua lista está vazia :(')
        for indice, nome in enumerate(lista):
            nome = nome.capitalize()
            print('#', indice, ' - ', nome)
    else:
        os.system('clear')
        print('Bem-vindo a lista de compras!\n')
        print('*'*50, '\n')
        print('Você não digitou uma opção válida.')