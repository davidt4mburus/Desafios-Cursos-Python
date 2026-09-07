soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        soma += n
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

# Nesse cód criamos um laço de repetição FOR pedindo de 1 até 500 (e para pular de dois em dois). Em seguida, se o número do laço for divisivel por 3, ele soma todos e conta também quantos números foram somados.