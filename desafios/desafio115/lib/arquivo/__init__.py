from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt é read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+ é escrever arquivo e criar acaso não tenha
    except:
        print('Houve um erro na criação!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') #serve pra separar os dados
            dado[1] = dado[1].replace('\n', '') # removo a quebra de linha do cadastrar por nada
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # at é para adicionar texto
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print('Novo registro adicionado.')
            a.close()