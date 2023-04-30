"""
Esse é um tipo de calcukadora alteranativa ao apresentado no exercício 4.
"""

while True:
    ...
    #######
    sair = input('Caso deseje sair, digite [s]').lower().startswith('s')  # neste caso, '.islower' converte a str em str minúscula e 'startwith' verififica a condição

    if sair:
        break 