
hora = input('Favor digitar a hora atual (formato 24h): ')

while not hora.isdigit() or int(hora) > 23:
    hora = input('Formato da hora inválido. Favor inserir apenas o digito do horário (ex.: 2, 11, 17): ')

hora = int(hora)
print('')

if hora <= 11:
    print('Bom dia!')
elif hora < 17:
    print('Boa tarde!')
else:
    print('Boa noite!')
