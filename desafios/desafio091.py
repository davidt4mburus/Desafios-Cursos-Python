from random import randint
from time import sleep
from operator import itemgetter #O propósito dela é criar um "seletor" — uma espécie de instrução que diz "quando você me der um item, pegue a posição X dele".
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #o itemgetter diz pro sorted() "quando for comparar dois itens pra decidir a ordem, não olhe a tupla inteira — olhe só a posição 1 de cada uma" (ou seja, o valor do dado, ignorando o nome do jogador). É basicamente uma forma de dizer "ordene por isso aqui, especificamente".
print('-=' * 25)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)