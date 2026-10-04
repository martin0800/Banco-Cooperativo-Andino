from .empleado import Empleado


class Ejecutivo(Empleado):

    def __init__(self, rut, nombre):
        super().__init__(rut, nombre)

    def obtener_permisos(self):
        return [
            "Abrir cuentas",
            "Aprobar créditos"
        ]

    def abrir_cuenta(self):
        return "El ejecutivo puede abrir cuentas."

    def aprobar_credito(self):
        return "El ejecutivo puede aprobar créditos."