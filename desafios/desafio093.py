jogador = dict()
gols = list()
cont = 1
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    while cont <= partidas:
        gols.append(int(input(f'Quantos gols na partida {cont}: ')))
        cont += 1 
    break
jogador['gol'] = gols[:]
jogador['soma'] = sum(gols)
print('-=' * 25)
print(jogador)
print('-=' * 25)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}.')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for e, v in enumerate(jogador['gol']):
    print(f'  => Na partida {e+1}, fez {v} gols.')
print(f'Foi um total de {jogador["soma"]} gols.')