print('-'*15)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*15)

atual = 0
prox = 1
cont = 0
n = int(input('Quantos termos você quer mostrar? '))
while n > cont:
    print('{} → '.format(atual), end='')
    atual, prox = prox, atual + prox
    cont += 1
print('FIM!')

# Nesse programa perguntamos pro usuário quantos termos que ele quer que mostre. No while enquanto o n° de termos que usuário pediu for maior que o cont, ele vai fazer a seguinte operação: Na linha 11, o atual vale 0 e prox vale 1, só que ele adicional o valor do prox no atual e a operação atual + prox no prox. E na linha 10 ele exibe apenas o atual.