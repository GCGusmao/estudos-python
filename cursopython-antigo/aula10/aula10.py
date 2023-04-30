
nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')

idade = input('Qual a sua idade? ')

idade_minima = 18
idade_maxima = 30

print('')

if int(idade) > 120 or int(idade) < 0:
    print('Idade inválida!')
elif int(idade) >= idade_minima and int(idade) <= idade_maxima:
    print(f'Empréstimo autorizado para {nome} {sobrenome}.')
else:
    print(f'{nome} {sobrenome} não tem a idade mínima para solicitar um empréstimo.')
