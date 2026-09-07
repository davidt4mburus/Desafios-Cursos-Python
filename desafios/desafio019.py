import random
aluno1 = input('Digite nome do primeiro aluno: ')
aluno2 = input('Digite nome do segundo aluno: ')
aluno3 = input('Digite nome do terceiro aluno: ')
aluno4 = input('Digite nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = random.choice(alunos)
print('O aluno sorteado é {}'.format(aluno_sorteado))