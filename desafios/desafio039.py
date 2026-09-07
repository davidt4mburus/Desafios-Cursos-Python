print('*'*20)
print('ALISTAMENTO MILITAR')
print('*'*20)

nasc = int(input('Digite seu ano de nascimento: '))
ano_atual = 2026
idade = ano_atual - nasc

if idade < 18:
    menor = 18 - idade
    print('Você vai precisar se alistar em {} ano(s)'.format(menor))
elif idade > 18:
    maior = idade - 18
    print('Já se passou {} ano(s) para se alistar'.format(maior))
else:
    print('Você está com idade para se alistar!')