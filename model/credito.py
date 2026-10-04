from datetime import date
from .enums import EstadoCredito


class Credito:

    def __init__(self, id_credito, cliente, monto, estado=EstadoCredito.PENDIENTE):
        self.id_credito = id_credito
        self.cliente = cliente
        self.monto = monto
        self.estado = estado
        self.fecha = date.today()

    @property
    def id_credito(self):
        return self.__id_credito

    @id_credito.setter
    def id_credito(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del crédito debe ser un número positivo.")
        self.__id_credito = valor

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        if valor is None:
            raise ValueError("El crédito debe estar asociado a un cliente.")
        self.__cliente = valor

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El monto del crédito debe ser mayor que cero.")
        self.__monto = float(valor)

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, EstadoCredito):
            raise ValueError("Estado de crédito inválido.")
        self.__estado = valor

    def aprobar(self):
        self.estado = EstadoCredito.APROBADO

    def rechazar(self):
        self.estado = EstadoCredito.RECHAZADO

    def __str__(self):
        return (
            f"Crédito #{self.id_credito} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Monto: ${self.monto:,.0f} | "
            f"Estado: {self.estado.value}"
        )