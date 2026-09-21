from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class churrasco:
    consumo:float = 0.400
    preco:float = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def calcular_qtd_carne(self) -> float:
        return self.quant * churrasco.consumo

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * churrasco.preco

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quant

    def analisar(self):
        conteudo = f'Analisando {self.titulo} com {self.quant} convidados.'
        conteudo += f'\nCada participante comerá {churrasco.consumo}Kg e cada Kg custa R${churrasco.preco:,.2f}'
        conteudo += f'\nRecomendo comprar {self.calcular_qtd_carne():.3f}Kg de carne.'
        conteudo += f'\nO custo total será de R${self.calcular_custo_total():,.2f}'
        conteudo += f'\nCada convidado terá que pagar R${self.calcular_custo_individual():,.2f} para participar.'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

p1 = churrasco(titulo='Churras dos amigos', quant=15)
p1.analisar()