num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')

# Nesse programa o cód pede pro usuário um n°. Em seguida, ele cria um laço de repetição de 1 até o número digitado pelo usuário (foi adicionado +1 porque o programa só lê até um número antes do digitado). Se o número digitado for divisível pelo c e o resultado for 0, então ele pinta os números de amarelo que são divisiveis pelo que o usuario digitou, além do tot que soma e depois mostra quando vezes o número foi divisivel. Se não, ele pinta os números de vermelho.