"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero1_str = input('Favor digitar um número: ')

try:
    condicao1 = float(numero1_str) % 2 == 0
    if condicao1:
        print(f'O número {float(numero1_str)} é par.')
    else:
        print(f'O núemro {float(numero1_str)} não é par.')

except:
    print('Você digitou um número inválido.')

hora_str = input('Agora digite que horas são [hh]: ')

try:
    hora_int = int(hora_str)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite!')
    else:
        print('Esse horário não está dentro das 24h de um dia (0h a 23h).')

except:
    print('Você não digitou um horário valido.')


nome = input('Agora escreva seu primeiro nome: ')

caracteries = len(nome)

if caracteries == 0:
    print('Você deixou o campo em branco.')
elif caracteries >= 1 and caracteries <= 4:
    print('Seu nome é curto.')
elif caracteries >= 5 and caracteries <= 6:
    print('Seu nome é normal.')
elif caracteries > 6:
    print('Seu nome é muito grande.')