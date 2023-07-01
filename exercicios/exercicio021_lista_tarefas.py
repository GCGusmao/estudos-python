# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def add_itens(todo_item):
    if not todo_item:
        print('Você não digitou nenhuma tarefa.')
        return
    itens_list.append(todo_item)

def remove_itens():
    if len(itens_list) < 1:
        return print('Você não tem itens para remover.')
    removed = itens_list.pop()
    itens_deleted.append(removed)


def return_itens():
    if len(itens_deleted) < 1:
        return print('Você não tem itens para restaurar.')
    restored = itens_deleted.pop()
    itens_list.append(restored)


itens_list = []
itens_deleted = []

print('You can exit the program any time, typing "exit."\n')

while True:
    option = input('Favor digitar a tarefa desejada, "desfazer" ou mesmo "refazer": ')

    if option == 'exit':
        break
    elif option == 'desfazer':
        remove_itens()
    elif option == 'refazer':
        return_itens()
    else:
        add_itens(option)

    print('')

    for item in itens_list:
        print(item)
    
    print('')
    # print(itens_deleted)
