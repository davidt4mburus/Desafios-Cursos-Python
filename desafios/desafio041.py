nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = 2026
idade = ano_atual - nasc

if idade <= 9:
    print('MIRIM!')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')