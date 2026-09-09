from time import sleep
c = ('\033[m',   # 0 - Sem Cor
'\033[0;30;41m',  # 1 - Vermelho
'\033[0;30;42m',  # 2 - Verde
'\033[0;30;43m',  # 3 - Amarelo
'\033[0;30;44m',  # 4 - Azul
'\033[0;30;45m',  # 5 - Roxo
'\033[0;30m'      # 6 - Branco
    );

def ajuda(opc):
    título(f'Acessando o manual do comando \'{opc}\'', 4)
    print(c[6], end='')
    help(opc)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

opcao = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    opcao = str(input('Função ou Biblioteca > '))
    if opcao.upper() == 'FIM':
        break
    else:
        ajuda(opcao)
título('ATÉ LOGO!', 5)