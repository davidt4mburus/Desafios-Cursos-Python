maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o {}° ano: '.format(c)))
    idade = 2026 - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} pessoa(s) são de maior.'.format(maior))
print('{} pessoa(s) são de menor.'.format(menor))

# Nesse programa primeiro criamos duas variáveis (maior e menor) com valor 0. Em seguida, foi criado o laço de repetição pro usuário poder digitar 7 anos. Depois na variável idade ele pega o ano atual e subtrai com o ano digitado pelo usuário. Se a idade for maior ou igual a 18, ele soma na variável maior, se não ele soma na variável menor. No final tem dois prints dizendo quantos são de maior e quantos são de menor.