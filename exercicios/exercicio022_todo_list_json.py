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

import os
import json


def add_itens(todo_item, todo_list):
    if not todo_item:
        print('Você não digitou nenhuma tarefa.')
        return
    todo_list.append(todo_item)

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

def read_file(files, file_path):
    try:
        data = files
        with open(file_path, 'r', encoding='utf8') as file:
            data = json.load(file)
    except FileNotFoundError:
        save_file(files, file_path)
    return data

def save_file(tasks, file_path):
    data = tasks
    with open(file_path, 'w', encoding='utf8') as file:
        data = json.dump(
            tasks, 
            file, 
            indent=2, 
            ensure_ascii=False
            )
    return data

FILE_PATH = './exercicios/exercicio022.json'
itens_list = read_file([],FILE_PATH)
itens_deleted = []

print('You can exit the program any time, typing "exit."\n')

while True:
    # os.system('clear')
    option = input('Favor digitar a tarefa desejada, "desfazer" ou mesmo "refazer": ')

    if option == 'exit':
        break
    elif option == 'desfazer':
        remove_itens()
    elif option == 'refazer':
        return_itens()
    else:
        add_itens(option, itens_list)

    print('')

    for item in itens_list:
        print(f'\t{item}')  # O \t cria uma indentação no print, usando f-stings
    
    print('')

    save_file(itens_list, FILE_PATH)
    # print(itens_deleted)
