jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    cont = 1
    while cont <= partidas:
        gols.append(int(input(f'Quantos gols na partida {cont}: ')))
        cont += 1 
    jogador['gol'] = gols[:]
    jogador['soma'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N: ')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gol']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-' * 40)
print('<< Volte Sempre! >>')