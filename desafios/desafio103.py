def ficha(j='<desconhecido>', gols=0):
    print(f'O jogador {j} fez {gols} gol(s) no campeonato.')


nameJogador = str(input('Nome do Jogador: '))
númgols = str(input('Número de Gols: '))
if númgols.isnumeric():
    númgols = int(númgols)
else:
    númgols = 0
if nameJogador.strip() == '':
    ficha(gols=númgols)
else:
    ficha(nameJogador, númgols)