"""
Interpolação básica de strings
s - string
d and i - int
f - float
x and X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.982345
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

#  %x converte o valor para hexa minúsculo;
#  %X converte o valor para hexa maiúsculo;
#  %08x preenche o hexa com "0" até ter 8 casas.

print('O hexadecinal de %d é %04x' % (1500, 1500))
