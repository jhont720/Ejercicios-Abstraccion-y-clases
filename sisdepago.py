from abc import ABC, abstractmethod
import math

class figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class circulo(figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class rectangulo(figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

print("ejercicio 3: figuras geometricas")
circulo = circulo(5)
rectangulo = rectangulo(4, 6)

print(f"circulo area: {circulo.calcular_area():.2f}")
print(f"circulo perimetro: {circulo.calcular_perimetro():.2f}")
print(f"rectangulo area: {rectangulo.calcular_area()}")
print(f"rectangulo perimetro: {rectangulo.calcular_perimetro()}")
print()