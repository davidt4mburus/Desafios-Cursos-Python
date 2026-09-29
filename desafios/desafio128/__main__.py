from termostato import *
from rich import inspect

def main():
    t1 = Termostato()
    try: #Tente isso
        t1.temperatura = 25.3
    except Exception as e: #Senão tente isso
        print(f'Houve um problema: {e}')

    print(f'A temperatura atual é de {t1.ftemperatura}')

if __name__ == '__main__':
    main()