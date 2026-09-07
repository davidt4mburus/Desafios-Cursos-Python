lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'A lista completa é {lista}.')
print(f'A lista de números pares são: {par}')
print(f'A lista de números ímpares são: {impar}')