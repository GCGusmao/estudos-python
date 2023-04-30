
nome = input('Favor, digite o seu nome: ')

while not nome.isalpha():
    nome = input('Seu nome não pode conter números ou estar em branco. Favor digite novamente: ')

print('')

digitos = len(nome)

if digitos <= 4:
    print('Seu nome é curto.')
elif digitos <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
