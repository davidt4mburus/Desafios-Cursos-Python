def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip() #trocou as vírgulas por ponto e remover espaços
        if entrada.isalpha() or entrada == '': #se for alfanumerico ou estiver vazio, retorna mensagem com erro
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)