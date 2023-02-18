#1. Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:

    def __init__(self, velocida_maxima: int, kilometraje: int):
        self.velocidad_maxima: int = velocida_maxima
        self.kilometraje: int = kilometraje