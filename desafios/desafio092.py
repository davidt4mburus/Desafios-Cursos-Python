from datetime import datetime
rh = dict()
rh['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
rh['carteira'] = int(input('Número da carteira de trabalho (0 se não tiver): '))
rh['idade'] = datetime.now().year - ano
if rh['carteira'] != 0:
    rh['contratação'] = int(input('Ano de contratação: '))
    rh['salário'] = float(input('Salário: R$'))
    rh['aposentadoria'] = rh['idade'] + ((rh['contratação'] + 35) - datetime.now().year)
print('-=' * 25)
for k, v in rh.items():
    print(f' - {k} tem o valor {v}.')