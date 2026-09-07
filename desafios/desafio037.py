num = int(input('Digite um número: '))
base_escolhida = int(input('Escolha em qual deseja converter: 1-Binário -- 2-Octal -- 3-Hexadecimal '))

if base_escolhida == 1:
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))
elif base_escolhida == 2:
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))
elif base_escolhida == 3:
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))