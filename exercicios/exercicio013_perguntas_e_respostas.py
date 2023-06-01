
 

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#print('Pergunta: Quanto é 2+2?')
#print('')
#print('Opções:')
acertos = 0
for i in perguntas:
    print(f"Pergunta: {i['Pergunta']}\n")
    print('Opções: ')
    for j in enumerate(i['Opções']):
        indice, nome = j
        print(f'{indice}) {nome}')
    resposta_usuario = input('Escolha uma opção: ')
    if i['Opções'][int(resposta_usuario)] == i['Resposta']:
        print('Você acertou!\n')
        acertos += 1
    else:
        print('Você errou!\n')

print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')

#input('Escolha uma opção: ')
#print('')
#print('')
