# Formatação de Strings: f-strings
nome = 'Gustavo Gusmão'
altura = 1.85
peso = 85
imc = peso / (altura ** 2)
linha_1 =  f'{nome} tem {altura:.2f} de altura,'  # uma das formações de strings é a definição de casas decimais.
linha_2 = f'pesa {peso} quilos e seu IMC é igual a:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
