import random
n_ale = [0, 1, 2, 3, 4, 5]
num = random.choice(n_ale)
escolhido = int(input('Adivinhe qual n°: '))
if escolhido == num:
    print('Parabéns! Você acertou!')
else:
    print('Que pena! Você errou! O número sorteado era {}'.format(num))