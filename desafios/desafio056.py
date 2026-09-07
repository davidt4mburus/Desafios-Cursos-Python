somaidade = 0
mediaidade = 0
maior_idade_homem = 0
homem_velho = ''
cont_mulheres20 = 0
for c in range(1, 5):
    print('***** {} Pessoa *****'.format(c))
    name = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_velho = name
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_velho = name
    if sexo in 'Ff' and idade < 20:
        cont_mulheres20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, homem_velho))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(cont_mulheres20))

# Nesse programa criamos o laço de repetição pro usuário inserir 4 nomes, idades e sexo (M/F). Após isso com a variável somaidade, utilizamos pra somar todas as idades e na linha 20 criamos a variavel mediaidade para calcular a media da soma da idade das 4 pessoas. Na linha 21 utilizamos um print pra exibir a média da soma das idades. Em seguida para saber idade e nome do homem mais velho, criamos um if que se c == 1 e sexo in 'Mm', então ele atribui na variavel maior_idade_homem o valor da idade e na variavel homem_velho o valor do name. Depois foi feito mais um if que se o sexo in 'Mm' and idade for maior que a variavel maior_idade_homem, então maior_idade_homem fica com valor da idade e homem_velho fica com valor de name. E na linha 22 tem um print pra exibir o nome e idade do homem mais velho. Por fim, na linha 18 foi criado o if que se sexo in 'Ff' e a idade for menor que 20, então ele soma mais 1 na variável cont_mulheres20. Na linha 23 tem um print mostrando a contagem de quantas mulheres tem menos de 20 anos.