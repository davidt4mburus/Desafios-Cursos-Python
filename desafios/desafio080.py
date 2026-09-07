valores = list()
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]: # índices negativos contam de trás pra frente, então -1 sempre pega o último elemento da lista, não importa o tamanho dela.
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores): # Cria um "ponteiro" de posição (pos), começando em 0, e um laço while que vai percorrer a lista posição por posição, do início, enquanto ainda não tiver passado do tamanho dela.
            if n <= valores[pos]:
                valores.insert(pos, n) # A cada posição, checa: "o número novo é menor ou igual ao valor que já está nessa posição?" Se for, significa que é aqui que ele deve entrar — usa .insert(pos, n) pra inserir o número exatamente nessa posição (empurrando os demais elementos pra frente)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1 # Se a condição anterior não foi verdadeira (o número novo ainda é maior que o valor dessa posição), avança pra próxima posição da lista, pra continuar procurando o lugar certo.
print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')