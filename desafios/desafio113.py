def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu encerrar o programa!\033[m')
            return 0
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu encerrar o programa!\033[m')
            return 0
        else:
            return n

numInt = leiaInt('Digite um número inteiro: ')
numReal = leiaReal('Digite um número real: ')
print(f'O valor inteiro digitado foi {numInt} e real foi {numReal}')