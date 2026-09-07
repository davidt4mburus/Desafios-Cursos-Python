n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))

# Nesse programa pedimos pro usuário digitar um n° para calcularmos seu fatorial. Depois criamos um while que enquanto o n° que o usuário digitou for maior que 0, ele vai multiplicando. Quando for menor que 0, ele sai do while e exige o resultado final.

# Outra forma de calcular o fatorial que o python disponibiliza
""" from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f)) """