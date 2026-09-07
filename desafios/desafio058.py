from random import randint
computador = randint (0, 10)
print('Sou seu computador... Acabei de pensar em um número de 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

# Nesse programa importamos o random e colocamos na variável computador um randint de 0 até 10. Na linha 5 criamos a variável acertou com valor False. Depois em while ele pede pro jogador um número, em seguida ele soma +1 na variável palpites e se o valor que o jogador inseriu for identico ao do computador, o acertou se torna True e acaba saindo do while. Se não, se o valor que o jogador jogar for menor que o valor do computador, ele exibe um print dizendo pra jogar um valor maior. Se o valor que o jogador jogar for maior que o valor do computador, então ele exibe um print pedindo pra jogar um valor menor.