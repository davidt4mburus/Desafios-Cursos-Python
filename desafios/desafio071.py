print('=' * 15)
print('BANCO TAMBURUS')
print('=' * 15)
ced_50 = ced_20 = ced_10 = ced_1 = resultado = 0

valor = int(input('Qual valor você deseja sacar? R$'))
while valor // 50:
    ced_50 += 1
    valor -= 50
while valor // 20:
    ced_20 += 1
    valor -= 20
while valor // 10:
    ced_10 += 1
    valor -= 10
while valor // 1:
    ced_1 += 1
    valor -= 1

if ced_50 > 0:
    print(f'Total de {ced_50} cédulas de R$50')
if ced_20 > 0:
    print(f'Total de {ced_20} cédulas de R$20')
if ced_10 > 0:
    print(f'Total de {ced_10} cédulas de R$10')
if ced_1 > 0:
    print(f'Total de {ced_1} cédulas de R$1')

print('=' * 51)
print('Volte sempre ao Banco Tamburus! Tenha um ótimo dia!')

""" print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor deseja sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!') """ #EXEMPLO DO PROF GUANABARA