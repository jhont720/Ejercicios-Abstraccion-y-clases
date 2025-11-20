from abc import ABC, abstractmethod

class vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def detener(self):
        pass

class coche(vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def mover(self):
        if self.encendido:
            self.velocidad = 60
            return f"{self.marca} {self.modelo} moviendose a {self.velocidad} km/h"
        return "primero enciende el coche"
    
    def detener(self):
        self.velocidad = 0
        return f"{self.marca} {self.modelo} se detuvo"

class bicicleta(vehiculo):
    def __init__(self, tipo):
        self.tipo = tipo
        self.velocidad = 0
    
    def mover(self):
        self.velocidad = 15
        return f"bicicleta {self.tipo} pedaleando a {self.velocidad} km/h"
    
    def detener(self):
        self.velocidad = 0
        return f"bicicleta {self.tipo} se detuvo"

print(" vehiculos")
mi_coche = coche("toyota", "corolla")
mi_bici = bicicleta("montaña")

print(mi_coche.encender())
print(mi_coche.mover())
print(mi_coche.detener())

print(mi_bici.mover())
print(mi_bici.detener())
print()