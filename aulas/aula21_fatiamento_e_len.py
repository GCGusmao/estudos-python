# Fatiamento de strings
# 012345678
# Olá mundo
#-987654321
# Fatiamento [i:f:p] [::]


variavel = 'Olá mundo'
print(variavel[4]) # mostra apenas o índice
print(variavel[4:]) # Mostra o índice até o final
print(variavel[4:8]) # Mostra o indíce até o proxímo índice
print(variavel[4:8:2]) # Passo, ou seja, de quantos em quantos caractéries ele vai contar
print(variavel[::-1]) # Inverte a string!!
print(len(variavel)) # Conta o número de caractéries de uma string