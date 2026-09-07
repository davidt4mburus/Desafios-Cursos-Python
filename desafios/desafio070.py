produto = ''
preco = soma = menor = contador_1000 = 0
produto_barato = ''
opcao = ''
print('-' * 15)
print('ATACADÃO BAMBU')
print('-' * 15)
while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    soma += preco # Soma total
    if menor == 0 and produto_barato == '':
        menor = preco
        produto_barato = produto
    else:
        if preco < menor:
            menor = preco
            produto_barato = produto
    if preco > 1000:
        contador_1000 += 1 #Produto mais de 1000 reais
    opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('----------FIM DO PROGRAMA----------')
print(f'O total da compra foi R${soma}')
print(f'Temos {contador_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor}.')