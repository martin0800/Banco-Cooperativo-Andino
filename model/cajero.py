from .empleado import Empleado


class Cajero(Empleado):

    def __init__(self, rut, nombre):
        super().__init__(rut, nombre)

    def obtener_permisos(self):
        return [
            "Recibir depósitos",
            "Realizar giros"
        ]

    def recibir_deposito(self):
        return "El cajero puede recibir depósitos."

    def realizar_giro(self):
        return "El cajero puede realizar giros."