sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

# Nesse programa criamos primeiro a variavel sexo que pede pro usuário digitar M ou F. No final, colocamos o strip para remover os espaços, colocar em maiúsculo a primeira letra que começa no indice 0. Em seguida criamos o while que se sexo não for 'MmFf', ele vai dizer que está inválido e pedir pro usuário repetir novamente. Quando o usuário digitar o valor correto, sairá do while e vai exibir o print dizendo o sexo que foi registrado.