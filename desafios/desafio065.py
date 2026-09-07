resp = 'S'
med = cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um n°: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
med = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, med))
print('O maior número é {} e o menor {}'.format(maior, menor))

# Nesse programa adicionamos a variável resp = 'S'. No while, enquanto o resp for igual a 'Ss', então ele pede um número pro usuário, ele soma esse número, faz o cont +1 e considera esse primeiro número o maior e menor. Depois ele pergunta se o usuário deseja continuar com [S/N]. Quando ele deseja continuar tudo se repete, porém o primeiro if vai dar False, então ele vê se o proximo número digitado é maior que o anterior ou menor. Nisso ele vai deixando maior número no maior e menor número no menor. Quando o usuário digitar N em resp, o programa vai calcular a media com a soma dividido por quantos números foram inseridos. Por último ele exibe a média e depois qual maior e menor valor.