#6. Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor).
#Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.

class Carta:

    CORAZON: str = "Corazón"
    TREBOL: str = "Trebol"
    ESPADA: str = "Espada"
    DIAMANTE: str = "Diamante"

    def __init__(self, valor: str, pinta: str):
        self.valor: str = valor
        self.pinta: str = pinta