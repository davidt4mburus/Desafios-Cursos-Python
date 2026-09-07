numbers = [[], []]
add = 0
for n in range(1, 8):
    add = int(input(f'Digite o {n}° valor: '))
    if add % 2 == 0:
        numbers[0].append(add)
    else:
        numbers[1].append(add)
numbers[0].sort()
numbers[1].sort()
print(f'Os números pares são: {numbers[0]}')
print(f'Os números ímpares são: {numbers[1]}')