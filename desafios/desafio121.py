from rich import print

class Caneta:

    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _: # Acaso não escolha nenhuma das anteriores, escrever com branco.
                escolha = '[white]'
        self.cor = escolha
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def quebrar_linha(self, qnt = 1):
        print('\n' * qnt, end='')

    def escrever(self, msg):
        if self.tampada:
            print(f':prohibited: A {self.cor}caneta[/] está tampada!')
        else:
            print(f'{self.cor}{msg}[/] ', end='')

c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')
c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá mundo!')
c1.quebrar_linha(2)
c2.escrever('Deu certo.')
c3.escrever('Isso ai Davisão!!!')
c3.quebrar_linha(3)