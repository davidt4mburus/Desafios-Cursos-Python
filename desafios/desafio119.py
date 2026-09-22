from rich import print
from time import sleep
from rich.traceback import install
install()

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas:int = paginas
        self.pagina_atual = 1

        print(f':open_book: Você acabou de abrir o livro [red]{self.titulo}[/] que tem {self.total_paginas} páginas no total. Você está na página [yellow]{self.pagina_atual}[/].')

    def avancar_paginas(self, qnt = 1):
        cont = 0
        for pg in range(0, qnt, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward: ', end='')
                sleep(0.3)
                cont += 1
        print(f'Você avançou {cont} páginas e agora está na página [yellow]{self.pagina_atual}[/].')
        if self.fim_do_livro():
            print(f':closed_book: Você chegou ao final do livro [red]{self.titulo}[/].')

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False


l1 = Livro(titulo='Águas Profundas', paginas=20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)