
import random

digito_aleatorio = ''

for k in range(9):
    digito_aleatorio += str(random.randint(0,9))
print(digito_aleatorio)

lista_cpf = []
cpf_raw = ''
contagem_1_digito = 10
contagem_2_digito = 11
digito_10 = 0
digito_11 = 0

while True:
    cpf_raw = digito_aleatorio

    for i in cpf_raw:
        try:
            i = int(i)
            lista_cpf.append(i)
        except ValueError:
            print('Caracterie removido: ', i)

    for j in lista_cpf[:9]:
        digito_10 += (j * contagem_1_digito)
        contagem_1_digito -= 1
        digito_11 += (j * contagem_2_digito)
        contagem_2_digito -= 1

    digito_10 = digito_10 * 10
    digito_10 = digito_10 % 11
    condicao_1 = (digito_10 <= 9)
    digito_10 = digito_10 if condicao_1 else 0

    digito_11 += (digito_10 * 2)
    digito_11 = digito_11 * 10
    digito_11 = digito_11 % 11
    condicao_1 = (digito_11 <= 9)
    digito_11 = digito_11 if condicao_1 else 0

    lista_cpf.append(digito_10)
    lista_cpf.append(digito_11)

    if digito_10 == lista_cpf[9] and digito_11 == lista_cpf[10]:
        print('PARABÉNS! Seu CPF é válido.')
    else:
        print('Oh no! Parece que você digitou um CPF inválido.')
    break