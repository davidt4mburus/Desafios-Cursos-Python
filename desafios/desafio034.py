salario = float(input('Digite o valor do seu salário: R$'))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Seu novo salário é de: R${}'.format(aumento))