cont = ('zero', 'um', 'dois', 'três', 'quatro', 
        'cinco', 'seis', 'sete', 'oito', 'nove', 
        'dez', 'onze', 'doze', 'treze', 'catorze', 
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 
        'dezenove', 'vinte')

""" while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Inválido. Tente novamente: ', end='')
print(f'Você digitou o número {cont[n]}.') """

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        resp = str(input((f'Você digitou o número {cont[n]}. Deseja continuar? [S/N] '))).upper().strip()[0]
        if resp == 'N':
            break
    else:
        print('Inválido. Tente novamente: ', end='')
print('Programa finalizado!')