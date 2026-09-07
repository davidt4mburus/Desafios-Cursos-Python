listagem = ('Caneta', 5.25,
            'Lápis', 4,
            'Borracha', 3.25,
            'Caderno', 30,
            'Estojo', 15.50,
            'Mochila', 75)
print('-' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)