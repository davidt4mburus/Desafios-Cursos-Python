from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, jogos):
        self.favoritos.append(jogos)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome real: [white on green] {self.nome} [/]'
        conteudo += f'\nJogos favoritos:'
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [green]{game}[/]'
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)
        print(painel)


j1 = Gamer(nome='David Tamburus', nick='dvd15')
j1.add_favoritos('Overwatch')
j1.add_favoritos('Lego Marvel')
j1.add_favoritos('Free Fire')
j1.ficha()