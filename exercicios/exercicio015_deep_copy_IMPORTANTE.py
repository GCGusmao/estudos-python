import copy


#  Função criada para aumentar os preços iterando sobre os valores.
def ajuste_precos(lista, ajuste, *args):
    
    nova_lista = copy.deepcopy(lista)

    for dicionario_novos_produtos in nova_lista:
        novo_preco = (dicionario_novos_produtos['preco'])*(1+(ajuste/100))
        novo_preco = round(novo_preco, 2)
        dicionario_novos_produtos.update(preco=novo_preco)
    return nova_lista


#  Função criada para aumentar os preços da lista utiizando list comprehension
def ajuste_precos_2(lista, ajuste, *args):
    novos_produtos = [  # estamos criando uma nova lista, para armazenar o dicionario.
        {**p, 'preco': round(p['preco'] * (1+(ajuste/100)), 2)} # estamos expandindo o dicionario com **p, regravando a nova chave "preco" e inserindo o valor ajustado pelo parâmetro informado pelo código.
        for p in copy.deepcopy(lista) #  estrutura do list comprehension, com o deep copy da lista de dicionários informados pelo código como parâmetro da função.
    ]
    return novos_produtos #  retornando a nova lista de dicionários criadas pela função

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = ajuste_precos_2(produtos, 50)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda valores: valores['nome'],
    reverse=True
)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda valores: valores['preco'],
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')