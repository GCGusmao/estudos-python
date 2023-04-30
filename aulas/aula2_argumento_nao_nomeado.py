print(12, 34) # no Python, isso é chamado de argumento não nomeado.
print()
print(56, 78)
print()

"""
Também podemos alterar o separador dentro de argumentos não nomeados, utilizando a seguinte estrutura.

sep="" -> define o separador dos argumentos, ou seja, a vírgula será substituida por isso.
end="" -> define o argumento que será executado no final de cada linha. Por padrão, o argumento executado é a quebra de linha "\n"

"""


print(12, 34, sep="-", end="##\n") # no Python, isso é chamado de argumento não nomeado.
print()
print(56, 78, sep=" && ") # tudo que estiver dentro das chaves será inserido, separando os argumentos não nomeados.
print()