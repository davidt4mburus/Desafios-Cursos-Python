def escreva(txt): #Adapta linhas com texto
    tam = len(txt) + 4 #Criar bordas para deixar centralizado
    print('↓' * tam)
    print(f'  {txt}')
    print('↑' * tam)

escreva('Olá, David Tamburus!')