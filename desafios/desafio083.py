frase = str(input('Digite a expressão: '))
pilha = []
for simb in frase:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() # Quando encontra um ), ele checa: tem algo na pilha pra "desempilhar"? Se sim, usa .pop()  que remove e retorna o último item da lista. Ou seja, cada ) "remove" um ( correspondente que já estava esperando na pilha.
        else:
            pilha.append(')') # Se encontrar um ) mas a pilha estiver vazia (nada pra remover), isso significa que apareceu um fechamento sem abertura correspondente — exatamente aquele problema que discutimos com ")("! Nesse caso, ele adiciona algo na pilha só pra "marcar" que deu erro, e usa break pra parar de processar
            break
if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')