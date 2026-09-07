print('*****LOJAS TAMBURUS*****')
preco = int(input('Digite o valor total das compras: '))
pag = int(input('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual opção deseja escolher? '''))
if pag == 1:
    desconto = preco * 0.1
    valor_final = preco - desconto
    print('Sua compra à vista no dinheiro/cheque com 10% de desconto fica em {}'.format(valor_final))
elif pag == 2:
    desconto = preco * 0.05
    valor_final = preco - desconto
    print('Sua compra à vista no cartão com 5% de desconto fica em {}'.format(valor_final))
elif pag == 3:
    valor_final = preco / 2
    print('Sua compra parcelada em 2x no cartão fica em {}'.format(valor_final))
elif pag == 4:
    juros = preco * 0.20
    valor_final = preco + juros
    opc_parc = (int(input('Deseja fazer em quantas parcelas? ')))
    parc = valor_final / opc_parc
    print("Sua compra vai ser parcelada em {}x de {} com juros. Sua compra de {} vai custar {} no final".format(opc_parc, parc, preco, valor_final))