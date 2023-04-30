"""
Validador de CPF #######

CPF = 168.995.350-09
-----------------------------------------------------
1 * 10 = 10                      #       1 * 11 = 11
6 * 9 = 54                       #       6 * 10 =
8 * 8 = 64                       #       8 * 9 =
9 * 7 = 63                       #       9 * 8 =
9 * 6 = 54                       #       9 * 7 =
5 * 5 = 25                       #       5 * 6 =
3 * 4 = 12                       #       3 * 5 =
5 * 3 = 15                       #       5 * 4 =
0 * 2 = 0                        #       0 * 3 = 0
                                 #       0 * 2 = 0 (valor encontrado para o dígito 1)
                                 #
somatório = 297                  #       Somatório = 343
11 - (297 % 11) = 11             #       11 - (343 % 11) = 9
Se valor > 9 = mudar para zero   #       Mesma regra! Dígito final = 9
Se valor < 9 = valor em questão  #

"""

loop = True

while loop:
    cpf_tratado = []
    cpf = input('Favor, digite o número do CPF: ')

    if cpf.isalpha():
        print('Você digitou algo diferente de um CPF. Você pode digitar tanto com pontos e traço quanto sem.')
        continue

    for v1 in cpf:
        if not v1 == '.' and not v1 == '-':
            cpf_tratado += v1

    qtd_digitos = len(cpf_tratado)
    # print(qtd_digitos)
    if qtd_digitos == 11:
        break
    else:
        pass


indice_1 = 0
somatorio_1 = 0

for i in range(10, 1, -1):
    somatorio_1 += (i * int(cpf_tratado[indice_1]))
    indice_1 += 1
#    print(somatorio_1)

digito_10 = 11 - (somatorio_1 % 11)
condicao_1 = (digito_10 <= 9)
digito_10 = digito_10 if condicao_1 else 0

indice_1 = 0
somatorio_1 = 0

for i in range(11, 2, -1):
    somatorio_1 += (i * int(cpf_tratado[indice_1]))
    indice_1 += 1
somatorio_1 = somatorio_1 + (digito_10 * 2)

digito_11 = 11 - (somatorio_1 % 11)
condicao_1 = (digito_11 <= 9)
digito_11 = digito_11 if condicao_1 else 0

# print(digito_10, digito_11)

condicao_validacao = (digito_10 == int(cpf_tratado[-2]) and digito_11 == int(cpf_tratado[-1]))
msg = "Parabéns, o CPF digitado é válido!!!" if condicao_validacao else f'O CPF não é válido, pois o digito' \
                                                                        f' {cpf_tratado[-2]} deveria ser igual a' \
                                                                        f' {digito_10}' \
                                                                        f' e o dígito {cpf_tratado[-1]}, igual a' \
                                                                        f' {digito_11}.'

print(msg)
