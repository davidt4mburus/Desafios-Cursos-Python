from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} [red]não pode acontecer[/].')

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'[white]{self.nome}[/] recebeu [red]{fator} de dano[/].')

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco Extraordinário', 'Golpe de Espada', 'Chute Duplo']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]{fator}[/] pontos de vida.')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Magia Negra', 'Adagas de Cristal', 'Chuva de Raios']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] realizou um feitiço de cura e recuperou [green]{fator}[/] pontos de vida.')