dias = int(input('Informe a quantidade de dias que o carro foi utilizado: '))
km = float(input('Informe a quantidade de KM rodado: '))
total_dias = dias * 60
total_km = km * 0.15
print('O valor total a se pagar é de R${:.2f}'.format(total_dias + total_km))