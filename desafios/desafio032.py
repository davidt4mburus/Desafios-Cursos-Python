ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('Ele é bissexto')
elif ano % 100 == 0 and ano % 400 == 0:
    print('Ele é bissexto')
else:
    print('Ele não é bissexto')