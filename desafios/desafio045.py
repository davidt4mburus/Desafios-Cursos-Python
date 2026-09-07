from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #COMPUTADOR JOGA PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCEU!')
    elif jogador == 2:
        print('Computador VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #COMPUTADOR JOGA PAPEL
    if jogador == 0:
        print('Computador VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #COMPUTADOR JOGA TESOURA
    if jogador == 0:
        print('Jogador VENCEU!')
    elif jogador == 1:
        print('Computador VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')