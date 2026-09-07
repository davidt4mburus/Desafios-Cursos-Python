cont = n = soma = 0
n = int(input('Digite um n° [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um n° [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi de {}.'.format(cont, soma))

# Nesse programa pedimos pro usuário inserir um n°. No while enquanto o n° for diferente de 999, ele adiciona o n° na soma e faz cont +1 e por último ele pede pra digitar o n° pro laço poder se repetir. Quando o usuário digitar 999, o 999 não vai ser adicionado na soma e nem no cont, pois antes dele somar e contar, ele da False no while e já pula pro print final.