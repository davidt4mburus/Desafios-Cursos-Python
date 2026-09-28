from rich import inspect
from classes026 import *

def main():
    f1 = FuncionarioMensalista(nome='José Luiz', salario_bruto=8500)
    f2 = FuncionarioHorista(nome='Lucas Oliveira', valor_hora=40, qtd_horas=150)
    f1.calcular_salario()
    f1.analisar_salario()
    f2.calcular_salario()
    f2.analisar_salario()


if __name__ == '__main__':
    main()