def metade(n=0):
    tot = n / 2
    return tot

def dobro(n=0):
    tot = n * 2
    return tot

def aumentar(n=0, taxa=0):
    total = n + (n * taxa/100)
    return total

def diminuir(n=0, taxa=0):
    total = n - (n * taxa/100)
    return total

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')# coloquei duas casas decimais na moeda e replace pra trocar os pontos por vírgula.