t = ()
for c in range (1, 5):
    n = int(input(f'Digite o {c}° valor: '))
    t += (n, )
print(f'Você digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)}')
if 3 in t:
    print(f'O valor 3 aparece na posição {t.index(3)+1}')
else:
    print('Não foi digitado valor 3.')
print(f'Os valores pares encontrados foram ', end='')
for x in t:
    if x % 2 == 0:
        print(x, end='')
    else:
        print('nenhum')
        break