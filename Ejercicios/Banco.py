#7. Cree una clase CuentaBancaria que contenga los siguientes atributos:
#numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#8. Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#9. Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#10. Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#11. Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.

class CuentaBancaria:

    def __init__(self, numero_cuenta: str, propietarios: str, balance: float):
        self.numero_cuenta: str = numero_cuenta
        self.propietarios: str = propietarios
        self.balance: str = balance

    def depositar(self, dinero: float):
        self.balance += dinero

    def retirar(self, dinero: float):
        if self.balance >= dinero:
            self.balance -= dinero

    def aplicar_cuota_manejo(self):
           self.balance *= 0.98

    def mostrar_detalles(self):
        print("DETALLE DE LA CUENTA")
        print(f"Número: {self.numero_cuenta}")
        print(f"Propietario: {self.propietarios}")
        print(f"Balance: {self.balance}")
