from classes027 import * 
from rich import inspect

def main():
    p1 = Guerreiro(nome='David', vida=1000)
    p2 = Mago('Lucas', vida=5000)

    p1.atacar(p2, forca=100)
    p2.atacar(p1, forca=250)
    p1.curar()
    p2.curar()



if __name__ == '__main__':
    main()