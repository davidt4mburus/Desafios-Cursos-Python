vel = int(input('Digite a velocidade: '))
if vel <= 80:
    print('Velocidade permitida. Pode seguir!')
else:
    v_multa = (vel - 80) * 7
    print('Velocidade acima do permitido. Você foi multado! O valor da multa é {} reais'.format(v_multa))
