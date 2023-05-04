"""
Faça uma lista de compras. O usuário pode:
Inserir valores, deletar valores e listar os itens da lista.
Não permita que o programa quebre com indices 
"""

import os

lista = []

print('Bem-vindo a lista de compras!\n')
print('*'*50, '\n')

while True:

    menu = input('Escolha [a]dicionar, [d]eletar ou mesmo [l]istar os itens: ').lower()

    if menu == 'a':
        lista.append(input('Digite o nome do item: '))
        print(lista)


    if menu == 'd':
        try:
            lista.pop(int(input('Digite o índice que deseja excluir: ')))
            print(lista)
        except:
            print('Você não digitou um valor válido, tente novamente.')

    if menu == 'l':
        for listar in lista:
            print(listar)