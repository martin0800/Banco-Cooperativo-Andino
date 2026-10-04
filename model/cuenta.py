from abc import ABC, abstractmethod
from datetime import date


class Cuenta(ABC):

    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.fecha_apertura = date.today()

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de cuenta no puede estar vacío.")
        self.__numero = valor.strip()

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        if valor is None:
            raise ValueError("La cuenta debe tener un cliente.")
        self.__cliente = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
           raise ValueError("El saldo debe ser numérico.")
        self.__saldo = float(valor)

    def depositar(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError("El monto del depósito debe ser mayor que cero.")

        self.__saldo += monto

    @abstractmethod
    def girar(self, monto):
        pass

    @abstractmethod
    def calcular_interes(self):
        pass

    def __str__(self):
        return (
            f"Cuenta: {self.numero} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Saldo: ${self.saldo:,.0f}"
        )