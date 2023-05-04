
nome1, nome2, nome3 = ['Maria', 'Luiz', 'Gustavo']

print(nome2)

valores1, *resto = ['São Paulo', 'Rio de Janeiro', 'Curitiba']

print(valores1, resto)


#  Por convenção, utiliza-se "_" para nomes de variáveis que você não vai utilizar em Python, como no exemplo abaixo.
_, cidade2, *_ = ['São Paulo', 'Rio de Janeiro', 'Curitiba']

print(cidade2)