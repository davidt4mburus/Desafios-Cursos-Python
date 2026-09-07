turma = dict()
turma['nome'] = str(input('Nome: '))
turma['media'] = float(input(f'Média de {turma["nome"]}: '))
print(f'O nome do(a) aluno(a) é {turma["nome"]}.')
print(f'Sua média foi {turma["media"]}')
if turma['media'] >= 7:
    turma['situação'] = 'Aprovado'
elif 5 <= turma['media'] < 7:
    turma['situação'] = 'Recuperação'
else:
    turma['situação'] = 'Reprovado'
print(f'Situação: {turma["situação"]}.')