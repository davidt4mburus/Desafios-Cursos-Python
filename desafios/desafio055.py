maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

# Nesse programa criamos duas variáveis (maior e menor) com valor 0. Em seguida foi criado o laço de repetição que o usuário informa 5 pesos. Como maior e menor não tem peso, o primeiro if atribui o valor do primeiro peso (tornando ele o maior e menor peso). Em seguida ele cai no else para poder comparar qual menor e qual maior com os pesos inseridos em seguida. Depois tem dois print cada um dizendo qual foi o maior e o menor peso.