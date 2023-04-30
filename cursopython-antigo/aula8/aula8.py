nome = 'Gustavo Gusmão'  # str
idade = 27  # int
altura = 1.75  # float
peso = 85.00  # float
ano_atual = 2021  # int
nascimento = (ano_atual - idade)
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura:.1f}m de altura e pesa {peso:.0f}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
