times = (
    'Flamengo', 'Palmeiras', 'São Paulo', 'Fluminense',
    'Botafogo', 'Athletico-PR', 'Atlético-MG', 'Grêmio',
    'Internacional', 'Cruzeiro', 'Fortaleza', 'Bahia',
    'Corinthians', 'Vasco', 'Bragantino', 'Santos',
    'Ceará', 'Sport', 'Juventude', 'Chapecoense'
)

print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')

print('-=' * 20)
print(f'Os 5 primeiros são: {times[:5]}')

print('-=' * 20)
print(f'Os últimos 4 colocados são: {times[-4:]}')

print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')

print('-=' * 20)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')