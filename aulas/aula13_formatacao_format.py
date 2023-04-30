a = 'A'
b = 'B'
c = 1.1
string = 'a={}, b={} e c={:.2f}'  # neste exemplo, dependemos da ordem dos itens
string = 'a={0}, b={1} e c={2:.2f}'  # neste exemplo, consutamos os índices dos argumentos
formato = string.format(a, b, c)

# nos também podemos nomear os argumentos, transformando-os em pârametros nomeados, da seguinte forma
string = 'a={nome1}, b={nome2} e c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)

