from classe031 import Retangulo
from rich import print, inspect

def main():
    r = Retangulo(1, 7)
    try:
        r.base = 12
        r.altura = 4 
        r.medidas = (3, 10)
    except Exception as e:
        print(f'[red]Ocorreu um erro do tipo {type(e).__name__}: {e}[/]')
    print(r.medidas)

if __name__ == '__main__':
    main()