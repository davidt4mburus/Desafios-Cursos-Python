from abc import ABC, abstractmethod

class Poligono:
    def __init__(self, lados):
        self.qnt_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
        pass

    def perimetro(self):
        pass

    def area(self):
        pass

class Circulo(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
        pass

    def perimetro(self):
        pass

    def area(self):
        pass