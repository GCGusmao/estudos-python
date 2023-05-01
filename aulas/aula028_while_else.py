"""
Uso do resurso exclusivo do Python de while/else
"""

string = 'Qualquer valor'

i = 0
while i< len(string):
    letra = string[i].lower()  #  garante que a letra sempre seja minuscula, para facilitar na verificação do código.

    if letra == 'k':
        break
    
    print(letra)
    i += 1
else:
    print('Não encontrei e letra "k" no seu texto.')  #  O bloco de código do else somente será executado caso o while seja finalizado.

print('O programa chegou ao fim.')