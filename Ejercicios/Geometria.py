#2. Cree una clase Punto que represente un punto en el plano cartesiano.
#3. Cree una clase Punto que represente un punto en el plano cartesiano.
#- Un método mostrar que imprima por consola las coordenadas del punto
#- Un método mover que cambie las coordenadas del punto
#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
#4. Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que
#definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
#5. Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con
#parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
import math
class Punto:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def mostrar(self):
        print(f"({self.x}, {self.y})")

    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
    def calcular_distancia(self, punto):
        distancia: float = math.sqrt((punto.y - self.y)** 2 + (punto.x - self.x)**2)
        return distancia

class rectangulo:

    def __init__(self, punto_1: Punto, punto_2: Punto):
        self.punto_1: Punto = punto_1
        self.punto_2: Punto = punto_2

    def calcular_perimetro(self):
        return (self.ancho() + self.alto()) * 2

    def ancho(self) -> float:
        return abs(self.punto_2.x - self.punto_1.x)

    def alto(self) -> float:
        return abs(self.punto_2.y - self.punto_1.y)





    def calcular_area(self):
        return self.ancho() * self.alto()

    def es_cuadrado(self):
        return self.ancho() == self.alto()

class Circulo:

    def __init__(self, centro: Punto, radio: float):
        self.centro: Punto = centro
        self.radio: float = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_promedio(self):
        return 2 * math.pi * self.radio

    def pertenece_a_circulo(self, punto: Punto) -> bool:
        termino_izq: float = (punto.x - self.centro.x) ** 2 + (punto.y - self. centro.y) ** 2
        return termino_izq <= self.radio ** 2

