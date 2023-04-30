nome = input('Qual o seu nome? ')  # função input sempre retorna uma string !!!
print(f'O seu nome é {nome=}')  # Esse "nome=" nos retorna o nome da variável + valor da variável.
print(f'O seu nome é {nome}')

print()
numero_1 = input('Agora digite um número: ')
numero_2 = input('Agora digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print()

print(f'A soma dos dois números é {int_numero_1 + int_numero_2}')
