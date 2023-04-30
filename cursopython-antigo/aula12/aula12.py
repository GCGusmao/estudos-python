
user = input('Digite um nome de usuário: ')
qtd_caractere = len(user)

if qtd_caractere < 6:
    print('Você digitou um usuário com menos de 6 caracteries. ')
else:
    print('Usuário cadastrado no sistema!')

first_cpf = input('Digite os primeiros 5 números do seu cpf: ')
last_cpf = input('Digite os últimos 6 números do seu cpf: ')

print(f'Seu CPF tem um toral de {len(first_cpf) + len(last_cpf)} núemros.')
