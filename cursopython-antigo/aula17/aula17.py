
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
usuario = input('Qual letra você quer maiúscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == usuario:
        nova_string += usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)