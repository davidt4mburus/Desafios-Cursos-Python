n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O número {} é o maior'.format(n1))
elif n2 > n1:
    print('O número {} é o maior'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, ambos são iguais!')