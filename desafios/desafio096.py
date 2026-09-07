def calc(larg, comp):
    area_total = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area_total}m²')

print('-' * 20)
print('CONTROLE DE TERRENOS')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
calc(l, c)