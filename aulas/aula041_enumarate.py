

nomes = ['Maria', 'Joao', 'Felipe', 'Ariely']

for indice, nome in enumerate(nomes):
    print(indice, nome)

for item in enumerate(nomes):
     indice, nome = item
     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')