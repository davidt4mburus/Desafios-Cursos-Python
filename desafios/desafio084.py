galera = list()
dados = list()
peso = list()
maior = menor = 0
r = ''
cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    cont += 1
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
print(f'Foram cadastradas {cont} pessoas.')
maior = max(peso)
menor = min(peso)
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for big in galera:
    if big[1] == maior:
        print(big[0])
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for little in galera:
    if little[1] == menor:
        print(little[0])