from classes033 import *

def main():
    a = Aluno(nome='David', nasc=2004, curso='ADS')

    a.add_curso('ads')
    print(a.cursos_oficiais)
    print(a.__dict__)

if __name__ == '__main__':
    main()