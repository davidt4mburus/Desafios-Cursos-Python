soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c))) #estou repetindo 6 vezes por causa do FOR
    if n % 2 == 0:
        soma += n
print('A soma dos números é de {}'. format(soma))

#Nesse cód criamos um laço de repetição FOR pedindo pro usuário inserir 6 números. Depois com o IF, realizamos a soma apenas dos números pares digitados pelo usuário.