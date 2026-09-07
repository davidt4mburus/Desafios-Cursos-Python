pessoa = dict()
galera = list()
média = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print('-=' * 25)
print(f'A) Foram cadastradas {len(galera)} pessoas.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas são: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}... ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')