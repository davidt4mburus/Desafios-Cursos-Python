from rich import print
from rich.panel import Panel

class ControleRemoto:
    """
Controle Remoto com as teclas de liga/desliga, aumentar/diminuir volume e avançar/voltar canal.
    """
    canal_min:int = 1
    canal_max:int = 5
    vol_min:int = 1
    vol_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def visual(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f':prohibited: A TV está [red]desligada[/]'
        else:
            conteudo = f'CANAL  ='
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f' [black on white] {canal} [/]'
                else:
                    conteudo += f' {canal} '

            conteudo += f'\nVOLUME = '
            for volume in range(ControleRemoto.vol_min, ControleRemoto.vol_max + 1):
                if volume <= self.volume_atual:
                    conteudo += '[black on green] [/]'
                else:
                    conteudo += '[black on black] [/]'

        tv = Panel(conteudo, title='[ TV ]', width=30)
        print(tv)

    def liga_desliga(self):
        self.ligado = not self.ligado

    def aumentar_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.vol_max:
                self.volume_atual += 1

    def diminuir_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.vol_min:
                self.volume_atual -= 1

    def avancar_canal(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def voltar_canal(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

c = ControleRemoto()
while True:
    c.visual()
    comando = str(input(f'< CH >  - VOL +\nTecla: '))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.avancar_canal()
        case '<':
            c.voltar_canal()
        case '-':
            c.diminuir_volume()
        case '+':
            c.aumentar_volume()