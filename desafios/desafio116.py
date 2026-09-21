from rich import print

class funcionario:
    """
Cadastra nome, setor e cargo de um funcionário.
    """

    # Atributos de Classe
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        # Atributos de Instância
        self.name = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f':victory_hand:  Olá, sou {self.name} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}.'


c1 = funcionario(nome='David', setor='TI', cargo='Desenvolvedor')
print(c1.apresentacao())

c2 = funcionario(nome='Lucas', setor='Saúde', cargo='Médico')
print(c2.apresentacao())