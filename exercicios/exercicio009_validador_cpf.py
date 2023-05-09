"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
lista_cpf = []
cpf_raw = ''
contagem_1_digito = 10
contagem_2_digito = 11
digito_10 = 0
digito_11 = 0

while True:
    cpf_raw = input('Por favor digite seu CPF: ')

    if len(cpf_raw) < 11 or len(cpf_raw) > 14:
        print('O valor digitado não condiz com um CPF. Favor colocar apenas números, pontos e traços')
        continue

    for i in cpf_raw:
        try:
            i = int(i)
            lista_cpf.append(i)
        except ValueError:
            print('Falha: ', i)

    if not len(lista_cpf) == 11: 
        print('Ops, encontramos um erro aqui. Você não parece ter digitado SOMENTE números no CPF. Tente novamente')
        continue

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

    print(digito_10, digito_11)
    break