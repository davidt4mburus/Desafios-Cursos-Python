words = ('DAVID', 'TAMBURUS', 'LUCAS', 'LUCIANA', 'OLIVEIRA',
        'ONILDA', 'SEBASTIAO', 'JONATAS')
for p in words:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=', ')