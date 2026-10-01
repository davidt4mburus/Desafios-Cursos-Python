from rich import inspect
from rich import print
from rich.traceback import install
#install() 

from diario import *

def main():
    d = Diario()
    d.escrever('Olá')
    d.escrever('Seja muito bem vindo.')
    try:
        d.ler('ABC')
    except Exception as e:
        print(f'[red]ERRO: {e}[/]')
    #inspect(d, private=True, methods=True)

if __name__ == '__main__':
    main()