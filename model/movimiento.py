from datetime import datetime
from .enums import TipoMovimiento


class Movimiento:

    def __init__(self, cuenta, tipo, monto, descripcion=""):
        self.cuenta = cuenta
        self.tipo = tipo
        self.monto = monto
        self.descripcion = descripcion
        self.fecha = datetime.now()

    @property
    def cuenta(self):
        return self.__cuenta

    @cuenta.setter
    def cuenta(self, valor):
        if valor is None:
            raise ValueError(
                "El movimiento debe estar asociado a una cuenta."
            )
        self.__cuenta = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, TipoMovimiento):
            raise ValueError("Tipo de movimiento inválido.")
        self.__tipo = valor

    @property
    def monto(self):
        return self.__monto

    @monto.setter
    def monto(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        self.__monto = float(valor)

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = str(valor).strip()

    def __str__(self):
        return (
            f"{self.fecha.strftime('%d-%m-%Y %H:%M')} | "
            f"{self.tipo.value} | "
            f"${self.monto:,.0f} | "
            f"{self.descripcion}"
        )