numbers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_col3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        numbers[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if numbers[l] [c] % 2 == 0:
            soma_par += numbers[l][c]
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{numbers [l] [c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {soma_par}')
for l in range(0,3):
    soma_col3 += numbers[l] [2]
print(f'A soma dos valores da terceira coluna é: {soma_col3}')
maior = max(numbers[1])
print(f'O maior valor da segunda linha é: {maior}')