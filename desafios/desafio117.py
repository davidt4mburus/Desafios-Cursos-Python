from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class produtos:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.valor:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)

p1 = produtos(nome='Iphone 13', valor=2800)
p1.etiqueta()

p2 = produtos(nome='Samsung S22', valor=2000)
p2.etiqueta()