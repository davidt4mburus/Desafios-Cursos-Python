def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    n: número a ser calculado
    show: True mostra a resolução do cálculo, False mostra apenas resultado
    return: O valor do fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, show=False))
help(fatorial)