
# Tuplas são listas com valores imutáveis, ou seja, não é possível inserir ou mesmo remover valores.

nomes = 'Maria', 'João', 'Pedro'
print(nomes[0])
print(nomes)

#  também é possível converter uma lista em uma tupla.

cidades = ['BSB', 'GYN', 'SDU']
cidades = tuple(cidades)
#  também é possível converter tuplas em listas
cidades = list(cidades)
print(cidades)