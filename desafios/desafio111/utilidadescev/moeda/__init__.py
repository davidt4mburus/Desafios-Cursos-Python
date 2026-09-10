def metade(n=0, format=False):
    tot = n / 2
    return tot if format is False else moeda(tot)

def dobro(n=0, format=False):
    tot = n * 2
    return tot if format is False else moeda(tot)

def aumentar(n=0, taxa=0, format=False):
    total = n + (n * taxa/100)
    return total if format is False else moeda(total)

def diminuir(n=0, taxa=0, format=False):
    total = n - (n * taxa/100)
    return total if format is False else moeda(total)

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')# coloquei duas casas decimais na moeda e replace pra trocar os pontos por vírgula.

def resumo(n=0, taxaA=0, taxaB=0):
    print('-' * 50)
    print('RESUMO DO VALOR'.center(50))
    print('-' * 50)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaA}% de aumento: \t{aumentar(n, taxaA, True)}')
    print(f'{taxaB}% de redução: \t{diminuir(n, taxaB, True)}')
    print('-' * 50)