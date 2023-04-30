nome = input('qual o seu nome? ')
idade = input('Qual a sua idade? ')

nascimento = 2021 - int(idade)  # cast para converter str para int.

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {nascimento}.')
