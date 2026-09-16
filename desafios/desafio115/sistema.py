from lib.interface import *
from lib.arquivo import *
from time import sleep
import os

pasta = os.path.dirname(os.path.abspath(__file__))
arq = os.path.join(pasta, 'cursoemvideo.txt') 

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)