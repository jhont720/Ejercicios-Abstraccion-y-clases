from abc import ABC, abstractmethod

class empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

class empleadoporhora(empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_sueldo(self):
        sueldo = self.horas_trabajadas * self.tarifa_por_hora
        if self.horas_trabajadas > 40:
            horas_extra = self.horas_trabajadas - 40
            sueldo += horas_extra * (self.tarifa_por_hora * 0.5)
        return sueldo

class empleadofijo(empleado):
    def __init__(self, nombre, salario_base, bonificacion=0):
        self.nombre = nombre
        self.salario_base = salario_base
        self.bonificacion = bonificacion
    
    def calcular_sueldo(self):
        return self.salario_base + self.bonificacion

print(" empleados")
empleado_hora = empleadoporhora("carlos lopez", 45, 20)
empleado_fijo = empleadofijo("maria gonzalez", 3000, 300)

print(f"{empleado_hora.nombre}: ${empleado_hora.calcular_sueldo():.2f}")
print(f"{empleado_fijo.nombre}: ${empleado_fijo.calcular_sueldo():.2f}")