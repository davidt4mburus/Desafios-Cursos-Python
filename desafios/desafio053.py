frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

# Nesse programa primeiro solicitamos uma frase pro usuário (colocamos strip para remover os espaços das pontas e upper para deixar tudo em maiúsculo). Em seguida criamos a variável palavras que pega a frase e divide ela em uma lista de palavras. Depois na variável junto para juntar todas as palavras da variável palavras. No laço de repetição ele conta(len) as letras da variavel junto (só que o len conta de quantas letras tem, então colocamos o -1 para ele começar em 0), em seguida colocamos -1 pro range chegar exatamente em 0, depois colocamos -1 para que em vez que ele ir pra frente somando, ele anda pra trás. Esse laço de repetição vai adicionando as letras de junto só que invertido. Coloquei um print pra dizer a frase junta e ela no inverso. E por último, se o inverso foi igual a ele junto, então temos um palíndromo, se não ele não é.