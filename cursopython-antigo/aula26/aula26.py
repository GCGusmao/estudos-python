def funcao1(saudacao, nome):
    print(saudacao, nome)


def funcao2(n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma)


def funcao3(numero, perc):
    numero += numero * (perc / 100)
    return numero


def funcao4(v1):
    if (v1 % 3) == 0 and (v1 % 5) == 0:
        return 'fizzbuzz'
    if (v1 % 3) == 0:
        return 'fizz'
    if (v1 % 5) == 0:
        return 'buzz'
    return v1


funcao1('Bom dia', 'Gustavo!')
print()
funcao2(5, 5, 5)
print()
valor = funcao3(100, 50)
print(valor)
print()
valor_2 = funcao4(15)
print(valor_2)
