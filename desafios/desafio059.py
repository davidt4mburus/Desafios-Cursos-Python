n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>>> Qual opção deseja escolher? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} com {} é igual à {}.'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação de {} com {} é igual à {}.'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')

print('Fim do programa! Volte sempre!')