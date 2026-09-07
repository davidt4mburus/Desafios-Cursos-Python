import random
aluno1 = input('Digite nome do primeiro aluno: ')
aluno2 = input('Digite nome do segundo aluno: ')
aluno3 = input('Digite nome do terceiro aluno: ')
aluno4 = input('Digite nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A sequência de alunos que vão apresentar o trabalho são {}'.format(alunos))