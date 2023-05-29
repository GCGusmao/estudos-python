""""
Crie uma função que duplica, triplica e quadriplica
o número recebido como parâmetro.

"""

def multiplica_valor_por_x (x_vezes):
    def equacao (valor):
        return valor * x_vezes
    return equacao

multiplica_2x = multiplica_valor_por_x(2)
multiplica_3x = multiplica_valor_por_x(3)
multiplica_4x = multiplica_valor_por_x(4)
multiplica_5x = multiplica_valor_por_x(5)
multiplica_10x = multiplica_valor_por_x(10)

print(f'O valor de 25 duplicado é {multiplica_2x(25)}.')
print(f'O valor de 25 triplicado é {multiplica_3x(25)}.')
print(f'O valor de 25 quadruplicado é {multiplica_4x(25)}.')
print(f'O valor de 25 quintuplicado é {multiplica_5x(25)}.')
print(f'O valor de 25 decaplicado é {multiplica_10x(25)}.')
