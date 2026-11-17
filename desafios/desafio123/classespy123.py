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
        self.qnt_lados = lados
        self.lado = 4

    def perimetro(self):
        return self.qnt_lados * self.lado

    def area(self):
        return self.qnt_lados * self.qnt_lados
    

class Circulo(Poligono):
    def __init__(self, lados):
        super().__init__(lados)
        self.pi = 3.1416

    def perimetro(self):
        return (self.pi * 2) * self.qnt_lados

    def area(self):
        return self.pi * (self.qnt_lados * self.qnt_lados)