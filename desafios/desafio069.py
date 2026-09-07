idade = maior = homens = mulheres_menor = 0
sexo = ''
opcao = ''
while True:
    print('-' * 10)
    print('CADASTRE UMA PESSOA')
    print('-' * 10)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        mulheres_menor += 1
    elif sexo == 'M':
        homens += 1
    print('=' * 10)
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 é {maior}.')
print(f'Total de homens cadastrados é {homens}.')
print(f'Total de mulheres com menos de 20 anos é {mulheres_menor}.')