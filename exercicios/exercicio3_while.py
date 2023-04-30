
nome = 'Gustavo Gusmão'
novo_nome = ''
tamanho = len(nome)
contador = 0

while contador < tamanho:
    novo_nome += '*' + nome[contador]
    print(novo_nome)
    contador += 1

novo_nome += '*'
print(novo_nome)