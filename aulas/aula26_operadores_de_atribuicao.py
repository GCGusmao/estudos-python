"""
Operadores de atrbuição

Para somar uma variável a ela mesma mais um valor -> +=
Para subtrair uma variável a ela mesma mais um valor -> -=
Para dividir uma variável a ela mesma mais um valor -> /=
Para multiplicar uma variável a ela mesma mais um valor -> *=
.
.
.
Ou seja, qualquer operador aritimetico + o operador de atribuicao.
"""

contador  = 0

while contador < 10:
    contador += 1
    print(contador)

print('ACABOU!')