numbers = list()
while True:
    n = int(input('Digite um valor: '))
    numbers.append(n)
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
print(f'Foram digitados {len(numbers)} elementos.')
numbers.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente são {numbers}')
if 5 in numbers:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')