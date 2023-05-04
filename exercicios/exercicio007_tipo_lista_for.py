"""
for in com listas
Exiba os índices, de forma automática, para uma dada lista.
"""
lista = ['Maria', 'Helena', 'Luiz', 1, 2, 3, True, None]

lista.append('Pedro')


#  essa é uma forma de escrever os indices.
i = 0

while i < len(lista):
    print(i)
    i += 1

#  outra forma de escrever os indices é:

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))