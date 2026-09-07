distancia = int(input('Digite a distância: '))
if distancia <= 200:
    curta = distancia * 0.50
    print('O preço da viagem é {:.2f} reais'.format(curta))
else:
    longa = distancia * 0.45
    print('O preço da viagem é {:.2f} reais'.format(longa))