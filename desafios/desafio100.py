from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 números da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {lista}, temos {soma}.')

números = list()
sorteia(números)
somaPar(números)