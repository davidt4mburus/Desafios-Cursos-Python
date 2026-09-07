print('-'*20)
print('SIMULADOR DE EMPRÉSTIMO')
print('-'*20)

valor_casa = float(input('Digite valor da casa: R$'))
salario = float(input('Digite valor do salário: R$'))
anos = int(input('Em quantos anos pretende pagar? '))

valor_mensal = valor_casa / (anos * 12)
limite = salario * 0.3

if limite >= valor_mensal:
    print('Empréstimo aprovado! O valor mensal a ser pago é de {:.2f}'.format(valor_mensal))
else:
    print('Empréstimo negado!')