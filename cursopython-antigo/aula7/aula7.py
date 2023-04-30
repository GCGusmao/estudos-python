nome = 'Gustavo Gusmão'
idade = 27  # int
altura = 1.75  # float
e_maior = idade > 18  # bool
peso = 85  # int
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
